text = input()
for s in text:
    if s.isupper():
        print(s.lower(), end="")
    elif s.islower():
        print(s.upper(), end="")

# print(input().swapcase)