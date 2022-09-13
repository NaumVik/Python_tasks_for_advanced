# task link: https://stepik.org/lesson/416759/step/3?unit=406267 (module 5.1 step 3)
# Напишите программу, которая транспонирует квадратную матрицу.
#
# Формат входных данных
# На вход программе подаётся натуральное число n — количество строк и столбцов в матрице,
# затем элементы матрицы.
#
# Формат выходных данных
# Программа должна вывести транспонированную матрицу.

row = int(input())
column = int(input())
matrix = []

for i in range(row):
    elem = [int(j) for j in input().split()]
    matrix.append(elem)

change_column = [int(j) for j in input().split()]

for k in range(row):
    matrix[k][change_column[0]], matrix[k][change_column[1]] = matrix[k][change_column[1]], matrix[k][change_column[0]]

for a in range(row):
    print(*matrix[a])





