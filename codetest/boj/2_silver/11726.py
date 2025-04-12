TARGET = 10_007
temp = [1, 2]
n = int(input())
ans = [0] * n
if n == 1:
    print(1)
else:
    ans[0] = 1
    ans[1] = 2

    for i in range(2, n):
        ans[i] = ans[i - 1] + ans[i - 2]
    
    print(ans[n - 1] % TARGET)