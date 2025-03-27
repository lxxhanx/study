n = int(input())
cnt_2 = 0
cnt_5 = 0
cnt_10 = 0
for i in range(1, n + 1):
    while i % 10 == 0:
        i //= 10
        cnt_10 += 1
    while i % 5 == 0:
        i //= 5
        cnt_5 += 1
    while i % 2 == 0:
        i //= 2
        cnt_2 += 1
ans = cnt_10 + min(cnt_2, cnt_5)
print(ans)

# def fac(n):
#     ans = 1
#     if n == 0 or n == 1:
#         return ans
#     while n != 1:
#         ans *= n
#         n -= 1
#     return ans

# print(fac(n))