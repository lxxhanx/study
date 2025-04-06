n = int(input())
lst = list(range(1, n+1))

while len(lst) != 1:
    lst.pop(0)
    if len(lst) == 1:
        break
    a = lst.pop(0)
    lst.append(a)

print(lst[0])