max = 0
ans = 0

for i in range(1, 10):
    data = int(input())
    if data > max:
        max = data
        ans = i

print(max)
print(ans)