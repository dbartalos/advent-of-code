#!/usr/bin/env python

import sys

current = 0
most = 0
totals = []

with open(sys.argv[1], 'r') as input_data:
  for line in input_data:
    if line != '\n':
      current += int(line)
    else:
      if current > most:
        most = current
      current = 0
    totals.append(current)
  print(sum(sorted(totals, reverse=True)[:3]))
