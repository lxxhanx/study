n, m = map(int, input().split())
x, y = 0, 0
maps = [input() for _ in range(n)]
# print(maps)
start = ""
min = 2501
while m - y >= 8:
    cnt = 0
    cnt2 = 0
    start = maps[x][y]
    is_odd = False
    if (x + y) % 2 != 0:
        is_odd = True
    for i in range(x, x + 8):
        for j in range(y, y + 8):
            if (i + j) % 2 == 0:
                if maps[i][j] != start:
                    cnt += 1
                if maps[i][j] == start:
                    cnt2 += 1
            else:
                if maps[i][j] == start:
                    cnt += 1
                if maps[i][j] != start:
                    cnt2 += 1
    if cnt < min:
        min = cnt
    if cnt2 < min:
        min = cnt2
    x += 1
    if n - x < 8:
        x = 0
        y += 1
print(min)