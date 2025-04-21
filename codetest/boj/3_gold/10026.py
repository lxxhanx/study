import sys
input = sys.stdin.readline

n = int(input())
maps = [input().strip() for __ in range(n)]
color_maps = []
diff = [(1, 0), (0, 1), (-1, 0), (0, -1)]
for line in maps:
    color_maps.append(line.replace("G", "R"))

maps = [list(item) for item in maps]
color_maps = [list(item) for item in color_maps]

def bfs(x, y, map):
    target = map[y][x]
    map[y][x] = "O"
    stack = [(x, y)]

    while stack:
        x, y = stack.pop()

        for dx, dy in diff:
            cur_x = x + dx
            cur_y = y + dy

            if 0 <= cur_x < n and 0 <= cur_y < n:
                if map[cur_y][cur_x] != target:
                    continue
                else:
                    stack.append((cur_x, cur_y))
                    map[cur_y][cur_x] = "O"
    
    return 1

cnt = 0
cnt_color = 0
for i in range(n):
    for j in range(n):
        if maps[i][j] == "O":
            continue
        else:
            cnt += bfs(j, i, maps)
        if color_maps[i][j] == "O":
            continue
        else:
            cnt_color += bfs(j, i, color_maps)

print(cnt, cnt_color)