n = int(input())
users = [input().split() for _ in range(n)]
users.sort(key=lambda x: int(x[0]))
for user in users:
    print(user[0], user[1])