n = int(input())
lst = []

for i in range(n):
    call = int(input())
    if call == 0:
        lst.pop()
    else:
        lst.append(call)
print(sum(lst))