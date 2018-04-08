#!/bin/python3

import sys

def countingSort(arr):
    l = max(arr)
    res = [0] * (l+1)
    for el in arr:
        res[el] += 1
    return res

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = countingSort(arr)
    print (" ".join(map(str, result)))
