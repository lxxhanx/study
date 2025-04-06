n = int(input())

max_5 = n // 5

ans = 10000
check = False
for i in range(max_5 + 1):
    temp = n
    temp -= i * 5
    if temp % 3 == 0:
        temp_ans = i + temp // 3
        if temp_ans < ans:
            check = True
            ans = temp_ans

if check:
    print(ans)
else:
    print(-1)