#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
x = number
if x < 0:
    x *= -1
while x >= 10:
    x = x % 10
if number < 0:
    x *= -1
if x < 6 and x != 0:
    print("Last digit of", number, "is", x, "and is less than 6 and not 0")
if x < 6 and x == 0:
    print("Last digit of", number, "is", x, "and is 0")
if x > 5:
    print("Last digit of", number, "is", x, "and is greater than 5")
