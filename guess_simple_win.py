#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

####################################################
# for buzzer
buzz_pin = (11)
GPIO.setup(buzz_pin,GPIO.OUT)   # Set buzz_pin's mode as output
Buzz = GPIO.PWM(buzz_pin,440)

# for led
led_pin = (37)
GPIO.setup(led_pin, GPIO.OUT)   # Set led_pin's mode as output
#
####################################################

def win():
    GPIO.output(led_pin, True)
    for i in range(1, 10):
        Buzz.start(50)
        Buzz.ChangeFrequency(500)
        time.sleep(0.2)
        Buzz.ChangeFrequency(600)
        time.sleep(0.2)
    Buzz.stop()
    GPIO.output(led_pin, False)

n = random.randint(1,10)

guess = int(raw_input("Enter an number from 1 to 10:"))
while n != "guess":
    print
    if guess < n:
        print "Guess is too low"
        Buzz.start(50)
        Buzz.ChangeFrequency(100)
        time.sleep(1)
        Buzz.stop()
        guess = int(raw_input("Enter an number from 1 to 10:"))
    elif guess > n:
        print "Guess is too high"
        Buzz.start(50)
        Buzz.ChangeFrequency(440)
        time.sleep(1)
        Buzz.stop()
        guess = int(raw_input("Enter an number from 1 to 10:"))
    else:
        print "You guessed it!"
        win()
        break
    print

GPIO.cleanup()
