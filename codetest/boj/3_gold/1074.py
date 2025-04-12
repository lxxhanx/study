n, r, c = map(int, input().split())
real_n = n
n = 2 ** n

r_cnt = 0
c_cnt = 0
s_x, s_y = 0, 0
e_x, e_y = n, n

temp = n * n
val_start = 0
val_end = temp - 1
base = 0
while val_start < val_end:
    x, y = (s_x + e_x) // 2, (s_y + e_y) // 2
    val_start = temp // 4
    val_end = temp - 1
    if r >= x and c >= y:
        val_start *= 3
        val_end = temp - 1
        s_x = x
        s_y = y
    elif r >= x:
        val_start *= 2
        val_end = temp // 4 * 3 - 1
        s_x = x
        e_y = y
    elif c >= y:
        val_start *= 1
        val_end = temp // 4 * 2 - 1
        s_y = y
        e_x = x
    else:
        val_start *= 0
        val_end = temp // 4 * 1 - 1
        e_x = x
        e_y = y
    base += val_start
    temp //= 4

print(base)