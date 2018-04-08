#!/bin/python3

import sys

def runningTime(arr):
    ret = 0
    for i in range(len(arr)):
        if i == 0:
            continue
        else:
            val = arr[i]
            k = i
            for j in reversed(range(0,i+1)):
                if arr[j] > val:
                    k = j
            if k != i:
                for j in reversed(range(k+1,i+1)):
                    arr[j] = arr[j-1]
                    ret += 1
                arr[k] = val
                
    return ret

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = runningTime(arr)
    print(result)
