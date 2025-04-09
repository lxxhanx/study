import sys
input = sys.stdin.readline

m = int(input())
ans = set()

for _ in range(m):
    op = input()
    if "add" in op:
        target = int(op.split()[1])
        ans.add(target)
    elif "remove" in op:
        target = int(op.split()[1])
        if target in ans:
            ans.remove(target)
    elif "check" in op:
        target = int(op.split()[1])
        if target in ans:
            print(1)
        else:
            print(0)
    elif "toggle" in op:
        target = int(op.split()[1])
        if target in ans:
            ans.remove(target)
        else:
            ans.add(target)
    elif "all" in op:
        ans = set(range(1, 21))
    else:
        ans = set()