#!/bin/python3

import sys

def lilysHomework(arr):

    sorted_arr = sorted(arr)
    helper_dic = dict()
    for i in range(len(arr)):
        if arr[i] != sorted_arr[i]:
            helper_dic[i] = arr.index(sorted_arr[i])

    nbr_swaps = 0
    for k1,v1 in helper_dic.items():
        if k1 == v1:
            continue
        else:
            print('swap {} with {}'.format(arr[k1], arr[v1]))
            nbr_swaps += 1
            for k2,v2 in helper_dic.items():
                if v2 == k1:
                    helper_dic[k2] = v1 

    return nbr_swaps

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = lilysHomework(arr)
    print(result)

