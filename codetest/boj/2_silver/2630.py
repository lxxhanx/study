import sys
input = sys.stdin.readline

def isBlue(arr, x, y):
    if arr[y][x] == 1:
        return True
    else:
        return False

def seperate(arr, x, y, n):
    if n == 1:
        if isBlue(arr, x, y):
            return 1, 0
        else:
            return 0, 1
    
    if all(isBlue(arr, cur_x, cur_y) for cur_y in range(y, y + n) for cur_x in range(x, x + n)):
        return 1, 0
    elif all(not isBlue(arr, cur_x, cur_y) for cur_y in range(y, y + n) for cur_x in range(x, x + n)):
        return 0, 1
    else:
        blue_cnt = 0
        white_cnt = 0
        pos = [[0, 0], [1, 0], [0, 1], [1, 1]]
        n //= 2
        for dx, dy in pos:
            cur_x = x + dx * n
            cur_y = y + dy * n
            temp = seperate(arr, cur_x, cur_y, n)
            blue_cnt += temp[0]
            white_cnt += temp[1]
        return blue_cnt, white_cnt

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = seperate(arr, 0, 0, n)
print(ans[1])
print(ans[0])