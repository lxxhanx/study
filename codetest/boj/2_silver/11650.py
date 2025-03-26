n = int(input())
num_lst = [list(map(int, input().split())) for _ in range(n)]
num_lst.sort(key=lambda x: (x[0], x[1]))
for a, b in num_lst:
    print(a, b)