a, b = map(int, input().split())
if a < b:
    a, b = b, a
temp_a, temp_b = a, b

gcd = 0
while True:
    if a < b:
        a, b = b, a
    temp = a % b
    if temp == 0:
        gcd = b
        break
    a = b
    b = temp

scm = temp_a * temp_b // gcd

print(gcd)
print(scm)