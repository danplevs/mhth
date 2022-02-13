import logging
import json
import board
import adafruit_dht
import psutil


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

def update_data():
    sensors = {"DHT11_l": get_DHT11(board.D4)}
    
    logging.basicConfig(level=logging.INFO)
    for sensor_name, sensor_data in sensors.items():
            with open(f"./data/{sensor_name}.json", mode="w+") as output_file:
                json.dump(sensor_data, output_file)
                logging.info(f"Dumped {sensor_name} data")

if __name__ == "__main__":
    update_data()
