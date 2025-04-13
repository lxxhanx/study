import sys
input = sys.stdin.readline

n = int(input())
lst = [int(input()) for _ in range(n)]
dp = [[0] * (n + 1) for _ in range(3)]

for v in range(1, n + 1):
    for k in range(1, 3):
        if k == 2:
            dp[k][v] = dp[1][v - 1] + lst[v - 1]
        else:
            dp[k][v] = max(dp[0][v - 1], dp[1][v - 2], dp[2][v - 2]) + lst[v - 1]

print(max(dp[1][n], dp[2][n]))