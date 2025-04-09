import sys
input = sys.stdin.readline

n, m = map(int, input().split())
not_known = set([input().strip() for _ in range(n)])
known = set([input().strip() for _ in range(m)])
ans = sorted(not_known.intersection(known))

print(len(ans))
for i in ans:
    print(i)