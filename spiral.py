s = input().split()
row = int(s[0])
column = int(s[1])
number = 1
counter = 0
matrix = [[0] * column for _ in range(row)]

i = 0
j = 0
column_const = column - 1
row_const = row - 1

while counter < (column * row):
    while j != column_const and matrix[i][j] == 0:
        matrix[i][j] = number
        number += 1
        counter += 1
        j += 1
    while i != row_const and matrix[i][j] == 0:
        matrix[i][j] = number
        number += 1
        counter += 1
        i += 1
    while j != 0 and matrix[i][j] == 0:
        matrix[i][j] = number
        number += 1
        counter += 1
        j -= 1
    while i != 0 and matrix[i][j] == 0:
        matrix[i][j] = number
        number += 1
        counter += 1
        i -= 1
    i += 1
    j += 1
    column_const -= 1
    row_const -= 1

for a in range(row):
    for b in range(column):
        matrix[a][b] = str(matrix[a][b])
        print(matrix[a][b].ljust(3), end=' ')
    print()

