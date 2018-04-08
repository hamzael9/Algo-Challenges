#!/bin/python3

import sys

def activityNotifications(expenditure, d):
    ret = 0
    for i in range(d,len(expenditure)):
        # Get the expenditure for latest d days
        latest_d = list()
        for j in range(1,d+1):
            latest_d.append(expenditure[i-j])
        # Sort and get median
        latest_d.sort()
        median = latest_d[int(len(latest_d)/2)+1]
        # Compare median with today's
        if expenditure[i] >= (median*2):
            ret += 1
        
    return ret

if __name__ == "__main__":
    n, d = input().strip().split(' ')
    n, d = [int(n), int(d)]
    expenditure = list(map(int, input().strip().split(' ')))
    result = activityNotifications(expenditure, d)
    print(result)
