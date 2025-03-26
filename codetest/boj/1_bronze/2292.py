n = int(input())
i = 0
ans = 1
while True:
    if n <= ans:
        print(i + 1)
        break
    i += 1
    ans += 6 * i