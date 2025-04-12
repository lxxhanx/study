import sys
input = sys.stdin.readline

n = int(input())
time_list = [list(map(int, input().split())) for _ in range(n)]
time_list.sort(key=lambda x: x[0])
time_list.sort(key=lambda x: x[1])

meeting = []
for i in time_list:
    if not meeting:
        meeting.append(i)
    else:
        end_time = meeting[-1][1]
        if i[0] >= end_time:
            meeting.append(i)

print(len(meeting))