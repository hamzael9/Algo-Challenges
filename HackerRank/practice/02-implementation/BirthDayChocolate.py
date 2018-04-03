#!/bin/python3

import sys

def solve(n, s, d, m):
    res = 0
    if n < m:
        return 0
    else:
        for i in range(n):
            #print('i = %d' % (i))
            tmp = []
            if s[i] > d:
                continue
            else:
                if i+m-1 < n:
                    for j in range(m):
                        tmp.append(s[i+j])
                    #print(tmp)
                    if sum(tmp) == d:
                        res += 1
    return res



n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
