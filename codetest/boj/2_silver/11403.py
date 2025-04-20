import sys
input = sys.stdin.readline

n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]
graph = {}

for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            if i in graph:
                graph[i].append(j)
            else:
                graph[i] = [j]

def bfs(v, target):
    stack = []
    if v in graph:
        stack.extend(graph[v])
        while stack:
            i = stack.pop(0)
            if visited[i]:
                continue
            visited[i] = True
            if i == target:
                return 1
            else:
                if i in graph:
                    stack.extend(graph[i])
    return 0


ans = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        visited = [False] * n
        ans[i][j] = bfs(i, j)

for i in range(n):
    print(*ans[i])