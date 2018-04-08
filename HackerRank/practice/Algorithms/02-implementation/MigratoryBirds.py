#!/bin/python3

import sys

def migratoryBirds(n, ar):
    un = set(ar)
    dic = {}
    for e in un:
        dic[e] = 1

    for a in ar:
        dic[a] += 1

    max_val = -1
    res = -1
    for key,val in dic.items():
        if val > max_val:
            max_val = val
            res = key
    return res

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)
