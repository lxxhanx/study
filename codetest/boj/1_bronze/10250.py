t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())
    cur_h = 1
    cur_w = 1
    while n > 1:
        n -= 1
        if cur_h < h:
            cur_h += 1
        else:
            cur_h = 1
            cur_w += 1
    if cur_w < 10:
        print(f"{cur_h}0{cur_w}")
    else:
        print(f"{cur_h}{cur_w}")