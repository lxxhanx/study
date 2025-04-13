import sys
input = sys.stdin.readline

t = int(input())
lst = [int(input()) for _ in range(t)]
maximum = max(lst)

p = [0] * (maximum + 1)

p[0] = 0

for i in range(1, maximum + 1):
    if i == 1:
        p[i] = 1
    elif i == 4:
        p[i] = 2
    else:
        p[i] = p[i - 1] + p[i - 5]

for i in lst:
    print(p[i])