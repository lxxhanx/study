maximum = -1
for i in range(1000, 100, -1):
    for j in range(1000, 100, -1):
        target = i * j
        temp = str(i * j)
        if temp == temp[::-1]:
            maximum = max(maximum, target)

print(maximum)