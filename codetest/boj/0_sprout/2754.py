score = input()
if "A" in score:
    ans = 4.0
elif "B" in score:
    ans = 3.0
elif "C" in score:
    ans = 2.0
elif "D" in score:
    ans = 1.0
else:
    ans = 0.0

if "+" in score:
    ans += 0.3
elif "-" in score:
    ans -= 0.3

print(ans)