target = 600851475143
prime_list = [2, 3, 5, 7, 11, 13]
i = 2
for test in range(14, target):
    for j in range(1, test):
        if test % j == 0:
            break
    else:
        prime_list.append(test)
print(len(prime_list))

div_prime_list = []
for prime in prime_list:
    if target % prime == 0:
        div_prime_list.append(prime)

print(div_prime_list[-1])