import sys
input = sys.stdin.readline

n = int(input())
maps = [list(map(int, list(input().strip()))) for __ in range(n)]
diff = [(1, 0), (0, 1), (-1, 0), (0, -1)]

housing = []

for y in range(n):
    for x in range(n):
        if maps[y][x] == 0:
            continue
        cnt = 1
        stack = [(x, y)]
        maps[y][x] = 0
        while stack:
            nx, ny = stack.pop()

            for dx, dy in diff:
                cur_x = nx + dx
                cur_y = ny + dy

                if 0 <= cur_x < n and 0 <= cur_y < n:
                    if maps[cur_y][cur_x] == 1:
                        maps[cur_y][cur_x] = 0
                        cnt += 1
                        stack.append((cur_x, cur_y))
        housing.append(cnt)

print(len(housing))
housing.sort()
for i in housing:
    print(i)