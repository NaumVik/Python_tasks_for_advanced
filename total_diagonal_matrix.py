n = int(input())
matrix = []
matrix_column = []


def find_total(matrix):
    total = sum(matrix[0])
    for i in range(1, len(matrix)):
        if sum(matrix[i]) == total:
            continue
        else:
            return False
    return True


def find_total_diagonal(matrix):
    total_main_diagonal = 0
    total_second_diagonal = 0
    for a in range(n):
        total_main_diagonal += matrix[a][a]
        total_second_diagonal += matrix[a][n - a - 1]
    if total_second_diagonal == total_main_diagonal:
        return True
    else:
        return False


def check_numbers(n, matrix):
    spis_numbers = [int(b) for b in range(1, n**2 + 1)]
    for c in range(n):
        for d in range(n):
            if matrix[c][d] in spis_numbers:
                spis_numbers.remove(matrix[c][d])
                continue
            else:
                return False
    return True


for i in range(n):
    elem = [int(j) for j in input().split()]
    matrix.append(elem)


for j in range(n):
    elem_column = []
    for k in range(n):
        elem_column.append(matrix[k][j])
    matrix_column.append(elem_column)

if check_numbers(n, matrix):
    if find_total(matrix) and find_total(matrix_column) and find_total_diagonal(matrix):
        print("YES")
    else:
        print("NO")
else:
    print("NO")

