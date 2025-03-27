t = int(input())
lst = []
for _ in range(t):
    k = int(input())
    n = int(input())
    lst.append((k, n))
ans = []
for i in range(15):
    temp = []
    for j in range(14):
        if i == 0:
            temp.append(j + 1)
        else:
            temp.append(sum(ans[i - 1][:j + 1]))
    ans.append(temp)

for k, n in lst:
    print(ans[k][n - 1])