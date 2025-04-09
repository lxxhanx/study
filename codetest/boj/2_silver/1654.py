import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lst = [int(input()) for _ in range(k)]
lst.sort(reverse=True)

s, e = 1, max(lst)

while s <= e:
    mid = (s + e) // 2

    cnt = 0
    for line in lst:
        cnt += line // mid
    
    if cnt >= n:
        s = mid + 1
    else:
        e = mid - 1

print(e)