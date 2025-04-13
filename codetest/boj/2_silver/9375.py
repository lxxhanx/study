import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    clothes = {}
    n = int(input())
    for _ in range(n):
        detail, part = input().split()
        if part in clothes:
            clothes[part].append(detail)
        else:
            clothes[part] = [detail]
    
    ans = 1
    for part in clothes.keys():
        ans *= len(clothes[part]) + 1
    ans -= 1

    print(ans)