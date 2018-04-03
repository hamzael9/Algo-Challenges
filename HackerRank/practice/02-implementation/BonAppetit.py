# Enter your code here. Read input from STDIN. Print output to STDOUT


def solve(n, k, costs, b):
    total = 0
    for i in range(n):
        if i != k:
            total += costs[i]

    diff = b - int((total/2))
    if diff == 0:
        return "Bon Appetit"
    else:
        return diff

n, k = input().strip().split(' ')
n, k = int(n), int(k)
costs = list(map(int, input().strip().split(' ')))
b = int(input().strip())

result = solve(n, k, costs, b)
print(result)
