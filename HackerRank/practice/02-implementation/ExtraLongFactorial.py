#!/bin/python3

import sys

def extraLongFactorials(n):
    if n == 1:
        return n
    else:
        return n * extraLongFactorials(n-1)

if __name__ == "__main__":
    n = int(input().strip())
    res = extraLongFactorials(n)
    print(res)
