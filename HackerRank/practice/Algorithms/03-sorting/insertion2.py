#!/bin/python3

import sys

def print_arr(arr):
	for el in arr:
		print(el, end=' ')
	print('')

def insertionSort2(n, arr):
    for i in range(n):
        if i == 0:
            continue
        else:
            val = arr[i]
            k = i
            for j in reversed(range(0,i+1)):
                if val < arr[j]:
                    #print('{} is less than {}'.format(val,arr[j]))
                    k = j
            if k != i:
                # insert element arr[i] (val) in arr[k]
                # first shift
                for j in reversed(range(k+1,i+1)):
                    arr[j] = arr[j-1]
                arr[k] = val
        print_arr(arr)



if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    insertionSort2(n, arr)

