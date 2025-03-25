n = int(input())
lst = list(map(int, input().split()))
cnt = 0
for i in lst:
    if i == 1:
        continue
    elif i < 4:
        cnt += 1
    else:
        is_prime = True
        for k in range(2, i):
            if i % k == 0:
                is_prime = False
                break
        if is_prime:
            cnt += 1
print(cnt)

# for-else 실습
# n = int(input())
# lst = list(map(int, input().split()))
# cnt = 0
# for i in lst:
#     if i == 1:
#         continue
#     elif i < 4:
#         cnt += 1
#     else:
#         for k in range(2, i):
#             if i % k == 0:
#                 break
#         else:
#             cnt += 1
# print(cnt)