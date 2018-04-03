#!/bin/python3

import sys

test = False

def print_matrix(matrix):
    for row in matrix:
        for el in row:
            print('{0} '.format(el), end='')
        print('')

def matrixRotation(matrix):
    nr = len(matrix)
    nc = len(matrix[0])
    # Initialize result matrix with zeros
    rotated = [0] * nr
    for i in range(len(matrix)):
        rotated[i] = [0] * nc
    # Start Matrix Rotation
    nbr_squares = int(min(nr,nc)/2)
    nr_square = nr
    nc_square = nc
    for i in range(nbr_squares):
        for ii in range(i,nr_square):
            #print('Row {0}'.format(ii))
            if ii == i:
                for k in range(i,nc_square-1):
                    rotated[ii][k] = matrix[ii][k+1]
                rotated[ii][nc_square-1] = matrix[ii+1][nc_square-1]
                rotated[ii+1][i] = matrix[ii][i]
            elif ii == nr_square - 1:
                for k in range(i,nc_square-1):
                    rotated[ii][k+1] = matrix[ii][k]
                rotated[ii][i] = matrix[ii-1][i]
            else:
                rotated[ii][i] = matrix[ii-1][i]
                rotated[ii][nc_square-1] = matrix[ii+1][nc_square-1]
        nr_square -= 1
        nc_square -= 1
    return rotated

if __name__ == "__main__":
    if test == True:
        matrix = [
        [1 , 2 , 3 , 4 , 5 , 6],
        [7 , 8 , 9 , 1, 2 , 3],
        [4 , 5 , 5 , 6 , 7 , 8],
        [9 , 2 , 6 , 1 , 3 , 4],
        [5 , 6 , 7 , 8 , 9 , 3],
        [1 , 2 , 3 , 4 , 5 , 6]
        ]
        r = 1
    else:
        m, n, r = input().strip().split(' ')
        m, n, r = [int(m), int(n), int(r)]
        matrix = []
        for matrix_i in range(m):
           matrix_t = [int(matrix_temp) for matrix_temp in input().strip().split(' ')]
           matrix.append(matrix_t)
    # Rotate r times
    for i in range(r):
        matrix = matrixRotation(matrix)
    # Print Result Matrix
    print_matrix(matrix)
