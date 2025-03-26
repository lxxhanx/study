n = int(input())
num_lst = list(map(int, input().split()))
m = int(input())
find_lst = list(map(int, input().split()))
num_lst.sort()

def find(t, s, e, lst):
    if s < 0 or e >= len(lst):
        return 0
    if s == e:
        if lst[s] == t:
            return 1
        else:
            return 0
    mid = (s + e) // 2
    if lst[mid] < t:
        return find(t, mid + 1, e, lst)
    elif lst[mid] > t:
        return find(t, s, mid, lst)
    else:
        return 1

ans_lst = [find(i, 0, len(num_lst) - 1, num_lst) for i in find_lst]
for i in ans_lst:
    print(i)