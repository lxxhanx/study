while True:
    sent = input()
    ans = []
    if sent == ".":
        break
    for i in sent:
        if i == "(" or i == "[":
            ans.append(i)
        elif i == ")":
            if not ans:
                print("no")
                break
            if ans.pop() == "(":
                continue
            else:
                print("no")
                break
        elif i == "]":
            if not ans:
                print("no")
                break
            if ans.pop() == "[":
                continue
            else:
                print("no")
                break
    else:
        if not ans:
            print("yes")
        else:
            print("no")