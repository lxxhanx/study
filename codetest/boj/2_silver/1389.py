n, m = map(int, input().split())

graph = {}

# 그래프 생성 부분
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

def bfs(v, target, visited, meeting):
    if v == target:
        meeting[target] = 0
    
    stack = []
    for i in graph[v]:
        stack.append((i, 1))
    visited[v] = True
    cnt = 1
    while stack:
        i, temp = stack.pop(0)
        if visited[i]:
            continue
        else:
            visited[i] = True
            meeting[i] = temp
            for j in graph[i]:
                stack.append((j, temp + 1))

result = float('inf')
result_node = n + 1
for i in range(1, n + 1):
    meeting = [float('inf')] * (n + 1)
    for j in range(1, n + 1):
        visited = [False] * (n + 1)
        bfs(i, j, visited, meeting)
    ans = sum(meeting[1:])
    if result > ans or (result == ans and result_node > i):
        result = ans
        result_node = i

print(result_node)