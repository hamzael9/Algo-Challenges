#!/bin/python3

import os
import sys

#
# Complete the breakingRecords function below.
#
def breakingRecords(score):
    nbr_low, nbr_high = 0 , 0
    low, high = score[0], score[0]
    for i in range(1,len(score)):
        if score[i] > high:
            high = score[i]
            nbr_high += 1
        elif score[i] < low:
            low = score[i]
            nbr_low += 1
    #print('%d %d' % (nbr_high,nbr_low) )
    return (nbr_high, nbr_low)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    score = list(map(int, input().rstrip().split()))

    result = breakingRecords(score)

    f.write(' '.join(map(str, result)))
    f.write('\n')

    f.close()
