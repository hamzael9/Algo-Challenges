#!/bin/python3

import sys

def gridSearch(G, P):
    check_index = 0
    check_col = -1
    for g in G:
        search_res = g.find(P[check_index])
        if search_res > -1:
            if check_col == -1:
                check_index += 1
                check_col = search_res
                if check_index == len(P) - 1:
                    return 'YES'
            else:
                if search_res == check_col:
                    check_index += 1
                    if check_index == len(P) - 1:
                        return 'YES'
                else:
                    check_col = -1
                    check_index = 0
        else:
            if check_col > -1:
                check_col = -1
                check_index = 0
    return 'NO'

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        R, C = input().strip().split(' ')
        R, C = [int(R), int(C)]
        G = []
        G_i = 0
        for G_i in range(R):
           G_t = str(input().strip())
           G.append(G_t)
        r, c = input().strip().split(' ')
        r, c = [int(r), int(c)]
        P = []
        P_i = 0
        for P_i in range(r):
           P_t = str(input().strip())
           P.append(P_t)
        result = gridSearch(G, P)
        print(result)
