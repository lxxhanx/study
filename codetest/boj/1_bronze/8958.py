t = int(input())
for _ in range(t):
    answer_list = input()
    answer = 0
    temp = 1
    for i in range(len(answer_list)):
        if answer_list[i] == "O":
            try:
                if answer_list[i - 1] == "O":
                    if i == 0:
                        continue
                    temp += 1
                    answer += temp
                else:
                    temp = 1
                    answer += temp
            except:
                temp = 1
                answer += temp

    print(answer)

# # 좀 더 쉬운 코드... ㅎㅎ
# t = int(input())
# for _ in range(t):
#     answer_list = input()
#     answer = 0
#     temp = 1
#     for i in answer_list:
#         if i == "O":
#             answer += temp
#             temp += 1
#         else:
#             temp = 1

#     print(answer)