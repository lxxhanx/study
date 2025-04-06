import sys
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    op = input()
    if "push" in op:
        target = op.split()[1]
        lst.append(target)
    elif "pop" in op:
        if not lst:
            print(-1)
        else:
            print(lst.pop())
    elif "size" in op:
        print(len(lst))
    elif "empty" in op:
        if lst:
            print(0)
        else:
            print(1)
    elif "top" in op:
        if not lst:
            print(-1)
        else:
            print(lst[-1])