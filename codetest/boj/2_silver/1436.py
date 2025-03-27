base = '666'
lst = []
for i in range(0, 10):
    lst.append(str(i) + base)
    lst.append(base + str(i))

lst = list(set(lst))

for k in range(3):
    temp = []
    for i in lst:
        for j in range(10):
            temp.append(str(j) + i)
            temp.append(i + str(j))
    lst.extend(temp)
    lst = list(set(lst))

lst = list(set(map(int, lst)))
lst.sort()
n = int(input())
print(lst[n - 1])