target = 100

sqr = 0
for i in range(1, target + 1):
    sqr += i ** 2

print(sum(range(1, target + 1)) ** 2 - sqr)