lst = []
for _ in range(10):
    temp = int(input()) % 42
    lst.append(temp)
print(len(set(lst)))