#!/bin/python3

import sys

def birthdayCakeCandles(n, ar):
    max_height = max(ar)
    nbr_candles = 0
    for i in range(n):
        if ar[i] == max_height:
            nbr_candles += 1
    return nbr_candles

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
