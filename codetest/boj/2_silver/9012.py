n = int(input())
lst = [input() for _ in range(n)]
for i in lst:
    temp = []
    for x in i:
        if x == "(":
            temp.append(x)
        elif x == ")":
            if not temp:
                print("NO")
                break
            if temp.pop() == ")":
                continue
    else:
        if not temp:
            print("YES")
        else:
            print("NO")