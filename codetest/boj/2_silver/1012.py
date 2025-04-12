import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    arr = [[0] * m for _ in range(n)]
    for _ in range(k):
        y, x = map(int, input().split())
        arr[x][y] = 1
    
    cnt = 0
    queue = []
    m, n = n, m
    for x in range(m):
        for y in range(n):
            if arr[x][y] == 1:
                arr[x][y] = 0
                cnt += 1
                queue.append([x, y])
                while queue:
                    cur_x, cur_y = queue.pop(0)
                    cur_x += 1
                    if cur_x < m:
                        if arr[cur_x][cur_y] == 1:
                            arr[cur_x][cur_y] = 0
                            queue.append([cur_x, cur_y])
                    cur_x -= 1
                    cur_y += 1
                    if cur_y < n:
                        if arr[cur_x][cur_y] == 1:
                            arr[cur_x][cur_y] = 0
                            queue.append([cur_x, cur_y])
                    cur_y -= 1
                    cur_x -= 1
                    if cur_x >= 0:
                        if arr[cur_x][cur_y] == 1:
                            arr[cur_x][cur_y] = 0
                            queue.append([cur_x, cur_y])
                    cur_x += 1
                    cur_y -= 1
                    if cur_y >= 0:
                        if arr[cur_x][cur_y] == 1:
                            arr[cur_x][cur_y] = 0
                            queue.append([cur_x, cur_y])
    
    print(cnt)