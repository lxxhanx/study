n = int(input())
size_list = list(map(int, input().split()))
t, p = map(int, input().split())
t_count = 0
p_count_div = n // p
p_count_res = n % p
for s in size_list:
    if s % t == 0:
        t_count += s // t
    else:
        t_count += s // t + 1
print(t_count)
print(p_count_div, p_count_res)