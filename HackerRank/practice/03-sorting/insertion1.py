#!/bin/python3

import sys

def print_arr(arr):
	for el in arr:
		print(el, end=' ')
	print('')

def insertionSort1(n, arr):
	v_to_sort = arr[n-1]
	for i in reversed(range(n)):
		if arr[i-1] > v_to_sort:
			if i > 0:
				arr[i] = arr[i-1]
			else:
				arr[i] = v_to_sort
				break
		else:
			arr[i] = v_to_sort
			break
		print_arr(arr)
	return arr


if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    res = insertionSort1(n, arr)
    print_arr(res)
