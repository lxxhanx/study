n = int(input())
scores = list(map(int, input().split()))
max = max(scores)
ans = []
for s in scores:
    ans.append(s / max * 100)
print(sum(ans) / n)