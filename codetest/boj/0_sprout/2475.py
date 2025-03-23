lst = list(map(int, input().split()))

ans = 0
for i in lst:
    ans += i ** 2

ans %= 10
print(ans)