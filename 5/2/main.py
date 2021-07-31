#!/usr/bin/env python3
import random

birthday_year = int(input('誕生年を入力'))

numbers = list(range(1, 25 + 1))
random.shuffle(numbers)

birthday_year_position = {'x': 0, 'y': 0}

for height in range(1, 5 + 1):
    for width in range(1, 5 + 1):
        number = numbers.pop(0)
        print(number, end='  ')
        if number == birthday_year:
            birthday_year_position['x'] = width
            birthday_year_position['y'] = height
    print(' ')

print('{}は{}行{}列にあります'.format(
    birthday_year,
    birthday_year_position['y'],
    birthday_year_position['x'])
)
