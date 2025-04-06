import sys
import math
input = sys.stdin.readline


n = int(input())
if n == 0:
    print(0)
else:
    lst = [int(input()) for _ in range(n)]
    lst.sort()
    person = math.floor(n * 0.15 + 0.5)
    if person == 0:
        ans = sum(lst) / len(lst)
    else:
        temp = lst[person:-person]
        ans = sum(temp) / len(temp)
    ans = math.floor(ans + 0.5)
    print(ans)