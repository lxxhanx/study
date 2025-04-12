import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
tomato_map = [list(map(int, input().split())) for _ in range(n)]
ans_map = [[-1] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]

q = deque()
direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]

for x in range(n):
    for y in range(m):
        if tomato_map[x][y] == 1:
            q.append([x, y])
            visited[x][y] = True
            ans_map[x][y] = 1

while q:
    x, y = q.popleft()
    for dx, dy in direction:
        cur_dx = x + dx
        cur_dy = y + dy
        if cur_dx < 0 or cur_dx >= n:
            continue
        if cur_dy < 0 or cur_dy >= m:
            continue
        if tomato_map[cur_dx][cur_dy] == 0 and not visited[cur_dx][cur_dy]:
            ans_map[cur_dx][cur_dy] = ans_map[x][y] + 1
            visited[cur_dx][cur_dy] = True
            q.append([cur_dx, cur_dy])

isAns = True
max = -1
for x in range(n):
    for y in range(m):
        if tomato_map[x][y] == 0 and ans_map[x][y] == -1:
            isAns = False
        if ans_map[x][y] > max:
            max = ans_map[x][y]

print(max - 1 if isAns else -1)