target = 10_001
prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
i = 32

while len(prime_list) != target:
    for prime in prime_list:
        if i % prime == 0:
            break
    else:
        prime_list.append(i)
    i += 1

print(prime_list[-1])