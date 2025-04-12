import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dps(graphs, v, visited):
    visited[v] = True
    if v in graphs:
        for i in graphs[v]:
            if not visited[i]:
                dps(graphs, i, visited)

n, m = map(int, input().split())

graphs = {}

for _ in range(m):
    a, b = map(int, input().split())
    if a in graphs:
        graphs[a].append(b)
    else:
        graphs[a] = [b]
    if b in graphs:
        graphs[b].append(a)
    else:
        graphs[b] = [a]

visited = [False] * (n + 1)
cnt = 0
for i in range(1, n + 1):
    if not visited[i]:
        dps(graphs, i, visited)
        cnt += 1

print(cnt)