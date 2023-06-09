#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
last_digit = number - (10 * int(number / 10))
result = "Last digit of " + repr(number) + " is " + repr(last_digit)
if last_digit > 5:
    print(f"{result} and is greater than 5")
elif last_digit == 0:
    print(f"{result} and is 0")
else:
    print(f"{result} and is less than 6 and not 0")
