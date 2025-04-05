import sys
input = sys.stdin.readline

n = int(input())
body_list = []
ans_list = [0] * n
for i in range(n):
    a, b = map(int, input().split())
    body_list.append([a, b, i])

for i in range(n):
    cnt = 0
    for j in range(n):
        if i == j:
            continue
        else:
            if body_list[i][0] < body_list[j][0] and body_list[i][1] < body_list[j][1]:
                cnt += 1
    ans_list[i] = cnt + 1

print(" ".join(list(map(str, ans_list))))