import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
maps = []
for _ in range(n):
    temp = list(map(int, input().split()))
    maps.extend(temp)

start = min(maps)
end = max(maps)
result_time = float('inf')
result_height = 0

for i in range(start, end + 1):
    add = 0
    remove = 0
    for block in maps:
        if i - block >= 0:
            add += i - block
        else:
            remove += block - i
    
    if add <= b + remove:
        time = 2 * remove + add
        if result_time > time or (result_time == time and result_height < i):
            result_time = time
            result_height = i

print(result_time, result_height)