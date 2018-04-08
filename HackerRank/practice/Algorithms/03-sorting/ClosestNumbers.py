#!/bin/python3

import sys

def closestNumbers(arr):
    arr.sort()
    min_diff = -1
    min_pairs = []
    for i in range(len(arr)-1):
        diff = arr[i+1] - arr[i]
        if min_diff == -1:
            min_diff = diff
        elif diff < min_diff:
            min_diff = diff
            min_pairs = [arr[i], arr[i+1]]
        elif diff == min_diff:
            min_pairs.append(arr[i])
            min_pairs.append(arr[i+1])
        else:
            continue
    return min_pairs
        
if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = closestNumbers(arr)
    print (" ".join(map(str, result)))
