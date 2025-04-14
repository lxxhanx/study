import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())
visited = [False] * (n + 1)
graph = {i: [] for i in range(1, n + 1)}

for _ in range(m):
    a, b = map(int, input().split())
    if a in graph:
        graph[a].append(b)
    else:
        graph[a] = [b]
    if b in graph:
        graph[b].append(a)
    else:
        graph[b] = [a]

def bfs(v):
    stack = []
    visited[v] = True
    print(v, end= " ")
    stack.extend(graph[v])
    
    for i in stack:
        if visited[i]:
            continue
        else:
            temp = graph[i]
            visited[i] = True
            stack.extend(temp)
            print(i, end=" ")

def dfs(v):
    if visited[v]:
        return
    else:
        visited[v] = True
        print(v, end=" ")
        stack = []
        graph[v].sort()
        stack.extend(graph[v])
        for i in stack:
            dfs(i)

dfs(v)
print()
visited = [False] * (n + 1)
bfs(v)