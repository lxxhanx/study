a, b, v = map(int, input().split())
day_up = a - b
cnt = 0
final_goal = v - a
if a >= v:
    cnt += 1
elif day_up >= final_goal:
    cnt += 2
elif final_goal % day_up == 0:
    cnt += final_goal // day_up + 1
else:
    cnt += final_goal // day_up + 2
print(cnt)