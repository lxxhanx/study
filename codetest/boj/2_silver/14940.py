import sys
input = sys.stdin.readline
n, m = map(int, input().split())
map_list = [list(map(int, input().split())) for _ in range(n)]
ans_list = [[-1] * m for _ in range(n)]
stack = []

for x in range(n):
    for y in range(m):
        if map_list[x][y] == 2:
            stack.append([x, y])
            start_point = [x, y]
            ans_list[x][y] = 0
        if map_list[x][y] == 0:
            ans_list[x][y] = 0
            

direction = [[0, 1], [1, 0], [-1, 0], [0, -1]]
cnt = -1

while stack:
    # print(stack)
    temp = []
    cnt += 1
    for i in range(len(stack)):
        x, y = stack[i]
        ans_list[x][y] = cnt
        for dx, dy in direction:
            cur_x = x + dx
            cur_y = y + dy
            # print(x, y, cur_x, cur_y)
            if cur_x < 0 or cur_x >= n:
                continue
            if cur_y < 0 or cur_y >= m:
                continue
            if cur_x == start_point[0] and cur_y == start_point[1]:
                continue
            if map_list[cur_x][cur_y] == 1 and ans_list[cur_x][cur_y] == -1 and [cur_x, cur_y] not in temp:
                temp.append([cur_x, cur_y])
    # print(stack)
    stack = temp
            

for i in ans_list:
    print(" ".join(list(map(str, i))))