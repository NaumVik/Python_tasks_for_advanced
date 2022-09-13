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





