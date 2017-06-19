#!/usr/bin/env python
import random
import time
import RPi.GPIO as GPIO

buzz_pin = (11)

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(buzz_pin,GPIO.OUT)

Buzz = GPIO.PWD(buzz_pin,440)

n = random.randint(1,10)

def buzz():
    Buzz.start(50)
    time.sleep(1)
    Buzz.stop()

while n != "guess":
    print ('Guess of a number from 1 to 10')
    guess = input()
    guess = int(guess)
    if guess < n:
        print "guess is too low"
        buzz()
    elif guess > n:
        print "Guess is too high"
        buzz()
    else:
        print "you guessed it"
        break
