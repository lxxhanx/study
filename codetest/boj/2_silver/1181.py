n = int(input())
str_lst = []
for _ in range(n):
    str_lst.append(input())
str_lst = list(set(str_lst))
str_lst.sort()
str_lst.sort(key=lambda x: len(x))
for i in str_lst:
    print(i)