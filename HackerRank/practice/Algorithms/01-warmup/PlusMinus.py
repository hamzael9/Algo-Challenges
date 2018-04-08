#!/bin/python3

import sys

def plusMinus(arr):
    p = 0
    n = 0
    z = 0
    for e in arr:
        if e > 0:
            p += 1
        elif e < 0:
            n+= 1
        else:
            z += 1
    print(p/len(arr))
    print(n/len(arr))
    print(z/len(arr))


if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    plusMinus(arr)
