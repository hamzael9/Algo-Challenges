#!/bin/python3

import sys

def staircase(n):
    for i in range(n):
        nbr_hashes = i+1
        nbr_spaces = n-i-1
        for j in range(nbr_spaces):
            print(' ', end='')
        for k in range(nbr_hashes):
            print('#', end='')
        print('')


if __name__ == "__main__":
    n = int(input().strip())
    staircase(n)
