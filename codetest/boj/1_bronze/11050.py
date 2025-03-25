n, k = map(int, input().split())
def fac(n, m):
    if n == 1 or n == 0:
        return m
    else:
        return fac(n - 1, n * m)
print(fac(n, 1) // (fac(n - k, 1) * fac(k, 1)))