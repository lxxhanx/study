a, b = map(int, input().split())

if a < b:
    ans = "<"
elif a > b:
    ans = ">"
else:
    ans = "=="

print(ans)