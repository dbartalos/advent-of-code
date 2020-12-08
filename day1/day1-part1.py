#!/usr/bin/env python

import sys

target = []

with open(sys.argv[1], 'r') as my_file:
    for line in my_file:
        number = int(line)
        target.append(2020 - number)
        if(number in target):
            print((2020 - number) * number)
