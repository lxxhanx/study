n, m = map(int, input().split())
maps = [input() for _ in range(n)]
visited = [[False] * m for _ in range(n)]

for i in range(len(maps)):
    if 'I' in maps[i]:
        y = i
        x = maps[i].find('I')

stack = []
stack.append((x, y))
visited[y][x] = True
diff = [(1, 0), (0, 1), (-1, 0), (0, -1)]
cnt = 0

while stack:
    base_x, base_y = stack.pop()

    for dx, dy in diff:
        cur_x = base_x + dx
        cur_y = base_y + dy

        if 0 <= cur_x < m and 0 <= cur_y < n:
            if maps[cur_y][cur_x] == "X":
                visited[cur_y][cur_x] = True
                continue
            if not visited[cur_y][cur_x]:
                if maps[cur_y][cur_x] == "P":
                    cnt += 1
                stack.append((cur_x, cur_y))
                visited[cur_y][cur_x] = True

if cnt == 0:
    print("TT")
else:
    print(cnt)