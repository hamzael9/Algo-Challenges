#!/bin/python3

import os
import sys


def get_multiples(arr, max_val):
    mul = []
    for el in arr:
        for i in range(101):
            tmp = el * i
            if tmp < max(arr):
                continue
            elif tmp > max_val:
                break
            else:
                if tmp not in mul:
                    mul.append(tmp)
    print(mul)
    to_rem = []
    for m in mul:
        print ("checking %d" % (m))
        for a in arr:
            print ('with %d' % (a))
            if m % a != 0:
                print( 'Problem %d with %d' % (m,a) )
                to_rem.append(m)
                break

    for e in to_rem:
        mul.remove(e)
    return mul

#
# Complete the getTotalX function below.
#
def getTotalX(a, b):
    mul_a = get_multiples(a, min(b))
    print(mul_a)
    res = 0
    for el in mul_a:
        tmp = 0
        for bi in b:
            if bi%el == 0:
                tmp += 1
        if tmp == len(b):
            res += 1
            print(el)
    return res

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()
