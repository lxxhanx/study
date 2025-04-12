import sys
input = sys.stdin.readline

n = int(input())
connect_dict = {}
line = int(input())
for _ in range(line):
    a, b = map(int, input().split())
    if a not in connect_dict:
        connect_dict[a] = [b]
    else:
        connect_dict[a].append(b)
    if b not in connect_dict:
        connect_dict[b] = [a]
    else:
        connect_dict[b].append(a)

if 1 not in connect_dict:
    print(0)
else:
    stack = []
    stack.extend(connect_dict[1])
    infection = [1]
    while stack:
        a = stack.pop(0)
        if a in connect_dict:
            for item in connect_dict[a]:
                if item in infection:
                    continue
                else:
                    stack.append(item)
        if a not in infection:
            infection.append(a)
    cnt = len(infection) - 1
    print(cnt)