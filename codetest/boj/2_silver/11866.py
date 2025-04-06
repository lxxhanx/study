n, k = map(int, input().split())
lst = list(range(1, n + 1))
cnt = 1
cur = 0
ans = []
while lst:
    if cur >= len(lst):
        cur = 0

    if cnt % k == 0:
        ans.append(lst[cur])
        lst.remove(lst[cur])
        cnt = 1
    else:
        cnt += 1
        cur += 1

print("<"+ ", ".join(list(map(str, ans))) + ">")