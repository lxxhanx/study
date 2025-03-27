a = input()
b = input()
c = input()
if a == "Fizz":
    if b == "Buzz":
        c = int(c)
        ans = c + 1
    else:
        b = int(b)
        ans = b + 2
elif a == "Buzz":
    if b == "Fizz":
        c = int(c)
        ans = c + 1
    else:
        b = int(b)
        ans = b + 2
elif a == "FizzBuzz":
    b = int(b)
    ans = b + 2
else:
    a = int(a)
    ans = a + 3

if ans % 3 == 0 and ans % 5 == 0:
    print("FizzBuzz")
elif ans % 3 == 0:
    print("Fizz")
elif ans % 5 == 0:
    print("Buzz")
else:
    print(ans)