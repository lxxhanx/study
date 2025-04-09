import sys
from math import floor
input = sys.stdin.readline

n = int(input())
num_lst = [int(input()) for _ in range(n)]

num_lst.sort()

num_count = {}
for num in num_lst:
    if num in num_count:
        num_count[num] += 1
    else:
        num_count[num] = 1

max_freq = max(num_count.values())
res = [k for k, v in num_count.items() if v == max_freq]
if len(res) == 1:
    ans = res[0]
else:
    res.sort()
    ans = res[1]

print(floor(sum(num_lst) / len(num_lst) + 0.5))
print(num_lst[len(num_lst) // 2])
print(ans)
print(max(num_lst) - min(num_lst))