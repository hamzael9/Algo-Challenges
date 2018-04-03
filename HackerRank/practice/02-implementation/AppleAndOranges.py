#!/bin/python3

import os
import sys

#
# Complete the countApplesAndOranges function below.
#
def countApplesAndOranges(s, t, a, b, apples, oranges):
    # calculate distances between house & trees
    a_s = s - a
    a_t = t -a
    t_b = b - t
    s_b = b - s
    # check if fruits fell in house
    nbr_apples = 0
    nbr_oranges = 0
    ## check apples
    for a in apples:
        if a > 0 and a >= a_s and a <= a_t:
            nbr_apples += 1
    for o in oranges:
        if o < 0 and -o >= t_b and -o <= s_b:
            nbr_oranges += 1
    print(nbr_apples)
    print(nbr_oranges)


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apple = list(map(int, input().rstrip().split()))

    orange = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apple, orange)
