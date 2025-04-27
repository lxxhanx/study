lst = [0] * 30
for _ in range(28):
    a = int(input())
    lst[a - 1] = 1

for i in range(len(lst)):
    if lst[i] == 0:
        print(i + 1)