n = int(input())
for i in range(1, n):
    num = str(i)
    s = i + sum([int(x) for x in num])
    if s == n:
        print(i)
        break
else:
    print(0)