#!/usr/bin/python

# Author: Orozco Hsu
# Date: 2017-05-19
# Org: DataService IoT training class sample

import RPi.GPIO as GPIO
import dht11
import time
import datetime

import requests, json

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# SAKS GPIO: 0/ BCM:17
instance = dht11.DHT11(pin=17)

# team id
sensorid = "team-a"

temperature = ""
humidity = ""

while True:
    result = instance.read()
    if result.is_valid():
        # print("DateTime: " + str(datetime.datetime.now()))
        # print("Temperature: %0.2f C" % float(result.temperature))
        temperature = "%0.2f" % float(result.temperature)
        # print("Humidity: %d" % result.humidity)
        humidity = "%d" % result.humidity
        
        # restful to inert data to cloud mysql
        try:
            if temperature != "" and humidity != "":
                endpoint = "http://172.104.90.53:6001/iot/%s/%s/%s" % (sensorid, str(temperature), str(humidity))
                # print endpoint
                requests.put(endpoint)
                print("Done: %s" %  (str(datetime.datetime.now())))

        except Exception as ex:
            print ex
    else:
        print("error")
    time.sleep(10)


