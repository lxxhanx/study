t = int(input())
for _ in range(t):
    r, s = input().split()
    r = int(r)
    for idx in s:
        print(idx * r, end="")
    print()