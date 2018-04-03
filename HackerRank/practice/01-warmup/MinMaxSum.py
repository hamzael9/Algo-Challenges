#!/bin/python3

import sys

def miniMaxSum(arr):
    min_index = arr.index(min(arr))
    max_index = arr.index(max(arr))
    min_total = 0
    max_total = 0
    for i in range(len(arr)):
        if i != min_index:
            max_total += arr[i]
    for i in range(len(arr)):
        if i != max_index:
            min_total += arr[i]

    print(min_total, max_total)

if __name__ == "__main__":
    arr = list(map(int, input().strip().split(' ')))
    miniMaxSum(arr)
