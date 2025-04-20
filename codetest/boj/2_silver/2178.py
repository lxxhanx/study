import sys
input = sys.stdin.readline

n, m = map(int, input().split())
maps = [input() for __ in range(n)]
diff = [(1, 0), (0, 1), (-1, 0), (0, -1)]
visited = [[False] * m for __ in range(n)]

def bfs(x, y):
    visited[y][x] = True
    stack = [(x, y, 1)]
    ans = float('inf')
    while stack:
        x, y, level = stack.pop(0)
        if (x, y) == (m - 2, n - 1) or (x, y) == (m - 1, n - 2):
            ans = min(ans, level)
        for dx, dy in diff:
            cur_x = x + dx
            cur_y = y + dy

            if 0 <= cur_x < m and 0 <= cur_y < n:
                if maps[cur_y][cur_x] == "0":
                    continue
                elif visited[cur_y][cur_x]:
                    continue
                else:
                    visited[cur_y][cur_x] = True
                    stack.append((cur_x, cur_y, level + 1))

    return ans + 1

print(bfs(0, 0))