#!/bin/python3

import sys


arr = []

def bigSorting(arr):
    return sorted(arr)

if __name__ == "__main__":
    n = int(input().strip())
    arr_i = 0
    for arr_i in range(n):
       arr_t = str(input().strip())
       arr.append(int(arr_t))
    result = bigSorting(arr)
    print ("\n".join(map(str, result)))
