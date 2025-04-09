import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

n_list.sort()

card_cnt = {}
for n in n_list:
    if n in card_cnt:
        card_cnt[n] += 1
    else:
        card_cnt[n] = 1
    
def bs(s, e, t, lst):
    if s < 0 or e >= len(lst):
        return 0
    if s == e:
        if lst[s] == t:
            return card_cnt[lst[s]]
        else:
            return 0
    mid = (s + e) // 2
    if lst[mid] > t:
        return bs(s, mid, t, lst)
    elif lst[mid] < t:
        return bs(mid + 1, e, t, lst)
    else:
        return card_cnt[lst[mid]]

res = []
card_list = list(card_cnt.keys())

for m in m_list:
    res.append(bs(0, len(card_list) - 1, m, card_list))

print(" ".join(list(map(str, res))))