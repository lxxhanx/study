import sys
input = sys.stdin.readline

n = int(input())
num_list = list(range(1, n + 1))
answer_list = [int(input()) for _ in range(n)]
stack = []
ans = []

cursor = 0

for i in answer_list:
    if i in stack:
        if stack[-1] == i:
            stack.pop()
            ans.append('-')
        else:
            print("NO")
            break
    else:
        stack.append(num_list[cursor])
        cursor += 1
        ans.append('+')
        if cursor >= n:
            pass
        else:
            while i + 1!= num_list[cursor]:
                stack.append(num_list[cursor])
                cursor += 1
                ans.append('+')
                if cursor >= n:
                    break
        stack.pop()
        ans.append('-')
else:
    for a in ans:
        print(a)