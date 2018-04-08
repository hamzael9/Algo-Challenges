#!/bin/python3

import sys

def lilysHomework(arr):

    sorted_arr = sorted(arr)
    helper_dic = dict()
    for i in range(len(arr)):
        helper_dic[arr[i]] = i

    nbr_swaps = 0
    for i in range(len(arr)):
        if arr[i] != sorted_arr[i]:
            pos = helper_dic[sorted_arr[i]]
            # swap arr[i] and arr[pos]
            tmp = arr[i]
            arr[i] = arr[pos]
            arr[pos] = tmp
            # update dic entry for arr[pos]
            helper_dic[arr[pos]] = pos
            nbr_swaps += 1
    
    return nbr_swaps

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = lilysHomework(arr)
    print(result)
