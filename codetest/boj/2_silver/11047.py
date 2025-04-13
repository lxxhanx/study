import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst = sorted([int(input()) for _ in range(n)], reverse=True)

cnt = 0
for i in lst:
    cnt += k // i
    k = k % i

print(cnt)