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
colors = [0xFF00, 0x00FF, 0x0FF0, 0xF00F]
led_pins = (37, 38)  # pins is a dict

GPIO.setup(led_pins, GPIO.OUT)   # Set pins' mode is output
GPIO.output(led_pins, GPIO.LOW)  # Set pins to LOW(0V) to off led

p_R = GPIO.PWM(led_pins[0], 2000)  # set Frequece to 2KHz
p_G = GPIO.PWM(led_pins[1], 2000)

p_R.start(0)      # Initial duty Cycle = 0(leds off)
p_G.start(0)
#
####################################################

def setColor(col):   # For example : col = 0x1122
        R_val = col  >> 8
        G_val = col & 0x00FF

        R_val = map(R_val, 0, 255, 0, 100)
        G_val = map(G_val, 0, 255, 0, 100)

        p_R.ChangeDutyCycle(R_val)     # Change duty cycle
        p_G.ChangeDutyCycle(G_val)

def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
 

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
        for col in colors:
            setColor(col)
        time.sleep(3)
        Buzz.stop()
        break
    print
