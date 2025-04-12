import sys
input = sys.stdin.readline

def fac(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fac(n - 1)

t = int(input())
for _ in range(t):
    n = int(input())
    cnt = 0
    ans = []
    for i in range(n + 1):
        for j in range(n + 1):
            for k in range(n + 1):
                if i + j * 2 + k * 3 == n:
                    ans.append([i, j, k])
    for item in ans:
        a = item[0]
        b = item[1]
        c = item[2]
        cnt += fac(a + b + c) // (fac(a) * fac(b) * fac(c))

    print(cnt)        