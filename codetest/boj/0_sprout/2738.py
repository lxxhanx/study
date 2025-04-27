n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
matrix_2 = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        print(matrix[i][j] + matrix_2[i][j], end=" ")
    print()