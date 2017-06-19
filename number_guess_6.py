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

def buzz(frequency,seconds):
    Buzz.start(50)
    Buzz.ChangeFrequency(frequency)
    time.sleep(seconds)
    Buzz.stop()

while n != "guess":
    print ('Guess of a number from 1 to 10')
    guess = input()
    guess = int(guess)
    if guess < n:
        print "guess is too low"
        buzz(100,1)
    elif guess > n:
        print "Guess is too high"
        buzz(400,1)
    else:
        print "you guessed it"
        for i in range(1, 10):
            buzz(500,0.2)
            buzz(600,0.2)
        break
