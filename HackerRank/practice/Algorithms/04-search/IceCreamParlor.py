#!/bin/python3

import sys

def icecreamParlor(m, arr):
    best = tuple()
    for i in range(len(arr)):
        diff = m - arr[i]
        for j in range(i+1, len(arr)):
            if arr[j] <= diff:
                if len(best) == 0:
                    best = (i+1, j+1)
                else:
                    s_new = arr[i] + arr[j]
                    s_old = arr[best[0]-1] + arr[best[1]-1]
                    if s_new > s_old:
                        best = (i+1, j+1)

    return sorted(best)
        

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        m = int(input().strip())
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        result = icecreamParlor(m, arr)
        print (" ".join(map(str, result)))

