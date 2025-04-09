import sys
readline = sys.stdin.readline

t = int(input())
n_list = [int(input()) for _ in range(t)]

maximum = max(n_list)
ans_dict = {0: (1, 0), 1: (0, 1)}

for i in range(2, maximum + 1):
    temp_1 = ans_dict[i - 1]
    temp_2 = ans_dict[i - 2]
    ans_dict[i] = (temp_1[0] + temp_2[0], temp_1[1] + temp_2[1])

for n in n_list:
    ans = ans_dict[n]
    print(ans[0], ans[1])