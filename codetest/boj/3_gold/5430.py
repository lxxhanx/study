import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    p = input().strip()
    reverse = 0
    while "RR" in p:
        p = p.replace("RR", "")
    n = int(input())
    lst = input().strip()[1:-1].split(',')
    back = 0
    front = 0
    try:
        for i in p:
            if i == "R":
                reverse ^= 1
            else:
                if reverse:
                    back += 1
                else:
                    front += 1
        if back + front > n:
            raise
        if back == 0:
            lst = lst[front:]
        else:
            lst = lst[front:-back]
        if reverse:
            lst = lst[::-1]
        
        if len(lst) == 0:
            print("[]")
        elif len(lst) == 1:
            print(f"[{lst[0]}]")
        else:
            for i in range(len(lst)):
                if i == 0:
                    print(f"[{lst[i]}", end=",")
                elif i == len(lst) - 1:
                    print(f"{lst[i]}]")
                else:
                    print(lst[i], end=",")
        
    except:
        print("error")