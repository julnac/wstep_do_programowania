from random import randrange


def generate_matrix(rows_number, columns_number):
    columns = []
    for x in range(1, columns_number + 1):
        rows = []
        for y in range(1, rows_number + 1):
            rows.append(randrange(5))
        columns.append(rows)
    return columns


def transpose_matrix(matrix):
    transposed_matrix = []
    for j in range(len(matrix[0])):
        new_row = []
        for i in range(len(matrix)):
            new_row.append(matrix[i][j])
        transposed_matrix.append(new_row)
    return transposed_matrix


if __name__ == "__main__":
    n = int(input("Podaj liczbę wierszy: "))
    m = int(input("Podaj liczbę kolumn: "))
    matrix = generate_matrix(n, m)
    print(matrix)
    print(transpose_matrix(matrix))
