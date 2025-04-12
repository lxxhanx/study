import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))
cum = [0] * (n + 1)
for i in range(len(lst)):
    cum[i + 1] = lst[i] + cum[i]

for _ in range(m):
    a, b = map(int, input().split())
    print(cum[b] - cum[a - 1])