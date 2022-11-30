#!/usr/bin/python3
import random
number = random.randint(-10, 10)
for i in range(number):
    if i > 0:
        print("{:d} is positive".format(number))
    elif i == 0:
        print("{:d} is zero".format(number))
    elif i < 0:
        print("{:d} is negative".format(number))
