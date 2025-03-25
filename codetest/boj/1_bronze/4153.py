while True:
    side_list = list(map(int, input().split()))
    if side_list == [0, 0, 0]:
        break
    side_list = sorted(side_list)
    if side_list[0] ** 2 + side_list[1] ** 2 == side_list[2] ** 2:
        print("right")
    else:
        print("wrong")