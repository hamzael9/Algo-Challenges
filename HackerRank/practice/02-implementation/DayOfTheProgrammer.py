#!/bin/python3

import sys

def is_julian(year):
    if year < 1918:
        return True
    else:
        return False


def is_leap(year):
    if is_julian(year):
        if year % 4 == 0:
            return True
        else:
            return False
    else:
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            return True
        else:
            return False


def solve(year):
    if year == 1918:
        return '26.09.1918'
    else:
        if is_leap(year):
            return '12.09.%d' % (year)
        else:
            return '13.09.%d' % (year)



year = int(input().strip())
result = solve(year)
print(result)
