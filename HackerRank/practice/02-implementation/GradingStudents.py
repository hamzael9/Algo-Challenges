#!/bin/python3

import sys

def solve(grades):
    rounded_grades = []
    tmp = 0
    for grade in grades:
        if grade < 38:
            tmp = grade
        else:
            m = grade % 5
            if m >= 3:
                tmp = grade + (5-m)
            else:
                tmp = grade
        rounded_grades.append(tmp)
    return rounded_grades

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))
