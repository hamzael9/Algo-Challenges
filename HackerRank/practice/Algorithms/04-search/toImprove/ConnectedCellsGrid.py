#!/bin/python3

import sys

'''
    Got 40pts, failed only test case 6
'''

testing = False

matrix = []
n = 0
m = 0


def traverse(i,j):
    size = 0
    for jj in range(j, m):
        if matrix[i][jj] == 1:
            matrix[i][jj] = -1
            size += 1
            # check surroundings (right,left,down,diagonal right)
            if jj+1 < m and matrix[i][jj+1] == 1:
                print('right') if testing == True else None
                size += traverse(i,jj+1)
            if jj > 0 and matrix[i][jj-1] == 1:
                print('left') if testing == True else None
                size += traverse(i,jj-1)
            if i+1 < n and matrix[i+1][j] == 1:
                print('down') if testing == True else None
                size += traverse(i+1,jj)
            if i+1 < n and jj+1 < m and matrix[i+1][jj+1] == 1:
                print('diago right') if testing == True else None
                size += traverse(i+1,jj+1)
            if i+1 < n and jj > 0 and matrix[i+1][jj-1] == 1:
                print('diago left') if testing == True else None
                size += traverse(i+1,jj-1)
            
            return size
                

def connectedCell():
    ret = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                size = traverse(i,j)
                if size > ret:
                    ret = size
    return ret           

if __name__ == "__main__":
    n = int(input().strip())
    m = int(input().strip())
    for matrix_i in range(n):
       matrix_t = [int(matrix_temp) for matrix_temp in input().strip().split(' ')]
       matrix.append(matrix_t)
    result = connectedCell()
    print(result)

