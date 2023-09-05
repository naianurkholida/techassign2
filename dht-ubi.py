from ubidots import ApiClient
import random
import time
import sys
import Adafruit_DHT

#Set the type of sensor and the pin for sensor
sensor = Adafruit_DHT.DHT11
pin = 17

# Create an ApiClient object

api = ApiClient(token='BBFF-Ood3ysjLnPC0jwaXj4R2Y6J5ZHV6Sv')

# Get a Ubidots Variable

try:
    temp = api.get_variable("64f5b8850616b28826ec812c")
    humid = api.get_variable("64f5b8850616b28826ec812b")

except ValueError:
    print("It is not possible to obtain the variable")

while True:
    try:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        print("Humidity: {:.1f} %".format(humidity))
        print("Temperature: {:.1f} °C".format(temperature))
        humid.save_value({'value': humidity})
        temp.save_value({'value': temperature})
        print("Value sent")
        time.sleep(120)
    except ValueError:
        print("Value not sent")
