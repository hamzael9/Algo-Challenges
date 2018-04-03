#!/bin/python3

import sys


arr = []

def quick_sort(arr, l, r):
    if r <= l:
        return

    pivot = arr[r]
    cur = l

    for i in range(l, r+1):
        if arr[i] <= pivot:
            tmp = arr[i]
            arr[i] = arr[cur]
            arr[cur] = tmp
            cur += 1
    print(arr)
    quick_sort(arr, l, cur-2)
    quick_sort(arr, cur, r)

def bigSorting(arr):
    quick_sort(arr, 0, len(arr)-1)

if __name__ == "__main__":
    n = int(input().strip())
    arr_i = 0
    for arr_i in range(n):
       arr_t = str(input().strip())
       arr.append(int(arr_t))
    bigSorting(arr)
    result = arr
    print ("\n".join(map(str, result)))
