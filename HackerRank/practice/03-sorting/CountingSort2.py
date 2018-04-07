#!/bin/python3

import sys

def countingSort(arr):
    # counting
    count = [0] * (max(arr) + 1)
    for el in arr:
        count[el] += 1
    # sorting
    res = []
    for i in range(len(count)):
        if count[i] > 0:
            for k in range(count[i]):
                res.append(i)
    return res

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = countingSort(arr)
    print (" ".join(map(str, result)))
