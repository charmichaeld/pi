#!/usr/bin/env python
import random
import time
import RPi.GPIO as GPIO

led_pin = (11)

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(led_pin,GPIO.OUT)

n = random.randint(1,10)

def flash_led():
    GPIO.output(led_pin, True)
    sleep(2)
    GPIO.output(led_pin, False)

while n != "guess":
    print ('Guess of a number from 1 to 10')
    guess = input()
    guess = int(guess)
    if guess < n:
        print "guess is too low"
    elif guess > n:
        print "Guess is too high"
    else:
        print "you guessed it"
        flash_led()
        break
