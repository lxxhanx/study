n = int(input())

ans = []
    
for i in range(n):
    if not ans:
        ans.append(0)
        ans.append(0)
    else:
        i += 1
        if i % 2 == 0 and i % 3 == 0:
            ans.append(min(ans[i//3], ans[i//2], ans[-1]) + 1)
        elif i % 2 == 0:
            ans.append(min(ans[i//2], ans[-1]) + 1)
        elif i % 3 == 0:
            ans.append(min(ans[i//3], ans[-1]) + 1)
        else:
            ans.append(ans[-1] + 1)

print(ans[n])