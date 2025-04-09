from math import sqrt
m, n = map(int, input().split())
num_list = list(range(m, n + 1))

def is_prime(x):
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    
    return True

for i in num_list:
    if i == 1:
        continue
    if is_prime(i):
        print(i)