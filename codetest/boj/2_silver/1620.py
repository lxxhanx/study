import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = []
dictionary = {}
for i in range(n):
    name = input().strip()
    lst.append(name)
    dictionary[name] = i + 1

for _ in range(m):
    op = input().strip()
    if op in dictionary:
        print(dictionary[op])
    else:
        print(lst[int(op) - 1])