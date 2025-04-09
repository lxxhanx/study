import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    cnt = 0
    while lst:
        if m == 0:
            temp = lst.pop(0)
            if not lst:
                cnt += 1
                print(cnt)
                break
            if max(lst) > temp:
                lst.append(temp)
                m = len(lst) - 1
            else:
                cnt += 1
                print(cnt)
                break
        else:
            temp = lst.pop(0)
            m -= 1
            if max(lst) > temp:
                lst.append(temp)
            else:
                cnt += 1
            