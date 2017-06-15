#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import random

####################################################
# for buzzer
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(11,GPIO.OUT)

Buzz = GPIO.PWM(11,440)
#
####################################################

####################################################
# for led
led_pin = (37)  # pins is a dict

GPIO.setup(led_pin, GPIO.OUT)   # Set pins' mode as output
GPIO.output(led_pin, GPIO.LOW)  # Set pins to LOW(0V) to turn off led

#
####################################################

n = random.randint(1,10)

guess = int(raw_input("Enter an number from 1 to 10:"))
while n != "guess":
    print
    if guess < n:
        print "Guess is too low"
        Buzz.start(50)
        time.sleep(1)
        Buzz.stop()
        guess = int(raw_input("Enter an number from 1 to 10:"))
    elif guess > n:
        print "Guess is too high"
        Buzz.start(50)
        time.sleep(1)
        Buzz.stop()
        guess = int(raw_input("Enter an number from 1 to 10:"))
    else:
        print "You guessed it!"
        GPIO.output(led_pin, GPIO.HIGH)
        time.sleep(3)
        GPIO.output(led_pin, GPIO.LOW)
        break
    print
