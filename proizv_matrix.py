# Task link: https://stepik.org/lesson/416756/step/10?unit=406264

n = int(input())
matrix1 = []
matrix2 = []

for a in range(n):
    elem = [int(a) for a in input().split()]
    matrix1.append(elem)
    matrix2.append(elem)


def proizv(matrix1, matrix2):
    n = len(matrix1)
    matrix_power = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for m in range(n):
                temp = matrix1[i][m] * matrix2[m][j]
                matrix_power[i][j] += temp
    return matrix_power


power = int(input())

for k in range(power - 1):
    matrix1 = proizv(matrix1, matrix2)

[print(*matrix1[i]) for i in range(n)]
