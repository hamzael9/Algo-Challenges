#!/bin/python3

import sys

'''
    Failed test cases 3 and 4 due to timeout :/
'''

def solve(a):

    if len(a) == 1:
        return 'YES'

    for i in range(1,len(a)-1):
        left = a[0:i]
        right = a[i+1:len(a)]
        sum_left = sum(left)
        sum_right = sum(right)
        if sum_left == sum_right:
            return 'YES'
        elif sum_left > sum_right:
            return 'NO'

    return 'NO'

T = int(input().strip())
for a0 in range(T):
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    result = solve(a)
    print(result)
