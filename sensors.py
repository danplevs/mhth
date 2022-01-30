import board
import adafruit_dht
import psutil


def get_DHT11(pin: board.pin = board.D4) -> dict:
    for proc in psutil.process_iter():
        if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
            proc.kill()

    try:
        device = adafruit_dht.DHT11(pin)
    except RuntimeError as error:
        raise error

    return dict(temperature=device.temperature, humidity=device.humidity)
