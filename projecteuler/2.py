target = 4_000_000
pre_i = 1
i = 1
sum = 0
while i < target:
    if i % 2 == 0:
        sum += i
    temp = pre_i
    pre_i = i
    i += temp
print(sum)