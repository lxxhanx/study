n = int(input())
line = list(map(int, input().split()))
ans = 0

start_index = 0
temp = {}

for i in range(len(line)):
    if len(temp) <= 2:
        if line[i] in temp:
            temp[line[i]] += 1
        else:
            temp[line[i]] = 1

    while len(temp) > 2:
        ans = max(ans, i - start_index)
        if line[start_index] in temp:
            if temp[line[start_index]] == 1:
                del temp[line[start_index]]
            else:
                temp[line[start_index]] -= 1
        start_index += 1

ans = max(ans, i - (start_index - 1))

print(ans)