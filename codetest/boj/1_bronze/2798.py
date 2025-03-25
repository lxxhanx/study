n, m = map(int, input().split())
card_list = list(map(int, input().split()))
max = 0
for i in range(len(card_list)):
    temp = m - card_list[i]
    if temp <= 0:
        continue
    else:
        for j in range(i + 1, len(card_list)):
            temp = m - card_list[i] - card_list[j]
            if temp <= 0:
                continue
            else:
                for k in range(j + 1, len(card_list)):
                    temp = m - card_list[i] - card_list[j] - card_list[k]
                    if temp < 0:
                        continue
                    elif temp == 0:
                        max = m
                    else:
                        if m - temp > max:
                            max = m - temp
print(max)