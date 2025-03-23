n, x = map(int, input().split())
a_list = list(map(int, input().split()))

for a in a_list:
    if a < x:
        print(a, end=" ")