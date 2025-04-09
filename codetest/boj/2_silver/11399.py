n = int(input())
time_list = list(map(int, input().split()))
time_list.sort(reverse=True)

cnt = 1
ans = 0
for t in time_list:
    ans += cnt * t
    cnt += 1

print(ans)