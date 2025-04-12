n, k = map(int, input().split())
dp = [0] * (k + 1)
if n == k:
    print(0)
else:
    for i in range(k + 1):
        if i <= n:
            dp[i] = n - i
        else:
            if i % 2 != 0:
                dp[i] = min(dp[i - 1] + 1, dp[(i + 1) // 2] + 2)
            else:
                dp[i] = min(dp[i - 1] + 1, dp[i // 2] + 1)

    print(dp[k])