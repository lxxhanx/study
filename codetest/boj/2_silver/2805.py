import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

result = 0
s = 0
e = max(trees)

while s <= e:
    mid = (s + e) // 2
    cut = 0
    for tree in trees:
        if tree <= mid:
            continue
        else:
            cut += tree - mid
    
    if cut >= m:
        result = mid
        s = mid + 1
    else:
        e = mid - 1

print(result)