import sys
input = sys.stdin.readline
n = int(input())
lst = {}
for _ in range(n):
    temp = int(input())
    try:
        if lst[temp]:
            lst[temp] += 1
    except:
        lst[temp] = 1
sorted_dict = dict(sorted(lst.items()))
for key, value in sorted_dict.items():
    for i in range(value):
        print(key)