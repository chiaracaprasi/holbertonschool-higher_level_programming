#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = abs(number) % 10
if ld > 5:
    print(f'The last digit of {number} is {ld} and and is greater than 5')
elif ld == 0:
    print(f'The last digit of {number} is {ld} and and is 0')
else:
    print(f'The last digit of {number} is {ld} and is less than 6 and not 0')
