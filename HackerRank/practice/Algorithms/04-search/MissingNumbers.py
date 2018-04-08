#!/bin/python3

import sys

def missingNumbers(arr, brr):
    dic_brr = dict()
    for el in brr:
        if el in dic_brr:
            dic_brr[el] += 1
        else:
            dic_brr[el] = 1
    dic_arr = dict()
    for el in arr:
        if el in dic_arr:
            dic_arr[el] += 1
        else:
            dic_arr[el] = 1
    
    res = []
    for k,v in dic_brr.items():
        if k not in dic_arr or dic_arr[k] != v:
            res.append(k)
    
    return res

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    m = int(input().strip())
    brr = list(map(int, input().strip().split(' ')))
    result = missingNumbers(arr, brr)
    print (" ".join(map(str, result)))
