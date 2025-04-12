import sys
input = sys.stdin.readline

n = int(input())
cnt = {}
tot = 0
lst = list(map(int, input().split()))
tup_lst = []
for i, val in enumerate(lst):
    if val in cnt:
        cnt[val] += 1
    else:
        cnt[val] = 1
        tot += 1
    tup_lst.append([val, i])

tup_lst.sort(key=lambda x: x[0])

ans = [0] * n

cur = 0

for i, item in enumerate(tup_lst):
    if i != 0 and tup_lst[i][0] != tup_lst[i - 1][0]:
        cur += 1
        
    val, id = item
    ans[id] = cur

print(" ".join(list(map(str, ans))))