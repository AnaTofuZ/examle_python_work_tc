#!/usr/bin/env python
import random

numbers = list(range(1, 101))

print(random.choices(numbers, k=10))
