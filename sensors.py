import logging
import json
import board
import adafruit_dht
import psutil
from apscheduler.schedulers.blocking import BlockingScheduler


scheduler = BlockingScheduler()


def get_DHT11(pin: board.pin) -> dict:
    for proc in psutil.process_iter():
        if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
            proc.kill()

    try:
        device = adafruit_dht.DHT11(pin)
        data = {"temperature": device.temperature, "humidity": device.humidity}
    except RuntimeError as error:
        print(error)

    return data

SENSORS = {"DHT11_l": get_DHT11(board.D4)}

@scheduler.scheduled_job("interval", minutes=5)
def main():
    for sensor_name, sensor_data in SENSORS.items():
            with open(f"./data/{sensor_name}.json", mode="w+") as output_file:
                logging.basicConfig(level=logging.INFO)
                json.dump(sensor_data, output_file)
                logging.info(f"Dumped {sensor_name} data")


scheduler.start()
