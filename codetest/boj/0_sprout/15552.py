import sys
input = sys.stdin.readline
n = int(input())
for __ in range(n):
    a, b = map(int, input().split())
    print(a + b)