#!/bin/python3

import sys

def quickSort(arr):
    p = arr[0]
    left = []
    right = []
    equal = []
    for el in arr:
        if el < p:
            left.append(el)
        elif el > p:
            right.append(el)
        else:
            equal.append(el)
    return left + equal + right

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = quickSort(arr)
    print (" ".join(map(str, result)))

