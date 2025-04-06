import sys
input = sys.stdin.readline

n = int(input())

queue = []

for i in range(n):
    op = input()
    if "push" in op:
        target = op.split()[1]
        queue.insert(0, target)
    elif "pop" in op:
        if not queue:
            print(-1)
        else:
            print(queue.pop())
    elif "size" in op:
        print(len(queue))
    elif "empty" in op:
        if not queue:
            print(1)
        else:
            print(0)
    elif "back" in op:
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif "front" in op:
        if not queue:
            print(-1)
        else:
            print(queue[-1])