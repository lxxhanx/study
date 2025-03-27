r = 31
M = 1234567891
L = int(input())
s = input()
hash = 0
for idx, c in enumerate(s):
    temp = ord(c) - 96
    hash += temp * (r ** idx)
hash %= M
print(hash)