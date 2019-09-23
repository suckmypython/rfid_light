import RPi.GPIO as GPIO
import logging
import time
import datetime
import os
from mfrc522 import SimpleMFRC522

good_code = 850439734127


try:
    print("Setting up pins")
    relay_status = False
    reader = SimpleMFRC522()
    print(reader)
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(20, GPIO.OUT)
    x = True
    while x is True:
        try:
            id, text = reader.read()
            if id == good_code:
                GPIO.output(20, GPIO.LOW)
                print(id)
                print("Light On")
                time.sleep(1)
            else:
                print("Wrong card!!! No Light on for you!!")
                pass
        except ValueError as e:
            print(e)
        try:
            id, text = reader.read()
            if id == good_code:
                GPIO.output(20, GPIO.HIGH)
                print(id)
                print("Light Off")
                time.sleep(1)
            else:
                print("Wrong card!!! No Light on for you!!")
                pass
        except ValueError as e:
            print(e)
except KeyboardInterrupt as e:
    GPIO.cleanup()
    print(e)
