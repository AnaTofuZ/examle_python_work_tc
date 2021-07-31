#!/usr/bin/env python3
import random

numbers = list(range(1, 25 + 1))
random.shuffle(numbers)

for height in range(1, 5 + 1):
    for width in range(1, 5 + 1):
        print(numbers.pop(0), end='  ')
    print(' ')
