#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
Last_digit = abs(number) % 10
if Last_digit > 5:
    print("Last digit of {} is {} and is greater than 5".format(Last_digit, number))
elif Last_digit == 0:
    print("Last digit of {} is {} and is 0".format(Last_digit, number))
elif Last_digit < 6 and Last_digit > 0:
    print("Last digit of {} is {} and is less than 6 and not 0".format(Last_digit, number))