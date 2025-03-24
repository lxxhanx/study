a = int(input())
b = int(input())
c = int(input())
ans = a * b * c
for i in range(10):
    print(str(ans).count(str(i)))