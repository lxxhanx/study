line = input()
minus_lst = line.split('-')
ans = []
for express in minus_lst:
    temp = list(map(int, express.split('+')))
    ans.append(sum(temp))

temp = ans[0]
for i in range(1, len(ans)):
    temp -= ans[i]

print(temp)