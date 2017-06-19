#!/usr/bin/env python
import random

n = random.randint(1,10)

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
        break
