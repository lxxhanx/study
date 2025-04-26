import math
ans = 1
for i in range(1, 21):
    ans = math.lcm(ans, i)

print(ans)