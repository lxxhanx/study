from math import sqrt

target = 2_000_000

def isPrime(n):
    if n == 1:
        return False
    elif n <= 3:
        return True
    else:
        k = 2
        temp = int(sqrt(n))
        while k <= temp:
            if n % k == 0:
                return False
            k += 1
        
        return True

ans = 0
for i in range(2, target + 1):
    if isPrime(i):
        print(i)
        ans += i

print(ans)