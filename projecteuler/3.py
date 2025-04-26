import math
target = 600851475143

maximum = int(math.sqrt(target))

print(maximum)

ans = []

for i in range(maximum, 2, -1):
    if target % i == 0:
        ans.append(i)
        a = target // i
        print(i, a)

print(ans)