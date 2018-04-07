#!/bin/python3

import sys

if __name__ == "__main__":
    n = int(input().strip())

    # Get input and initialize the dictionary
    dic = dict()
    half = n/2
    max_val = 0
    for a0 in range(n):
        x, s = input().strip().split(' ')
        x, s = [int(x), str(s)]
        if a0 < half:
            s = '-'
        if x in dic:
            dic[x].append(s)
        else:
            dic[x] = [s]
        if x > max_val:
            max_val = x

    # fill the helper array by counting
    helper = [0] * (max_val + 1) 
    for k,v in dic.items():
        helper[k] += len(v)

    # 
    for i in range(len(helper)):
        for el in dic[i]:
            print(el, end=' ')
