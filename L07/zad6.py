from random import randrange

rows_number_1 = int(input("Podaj liczbę wierszy 1 macierzy: "))
columns_number_1 = int(input("Podaj liczbę kolumn 1 macierzy: "))
rows_number_2 = int(input("Podaj liczbę wierszy 2 macierzy: "))
columns_number_2 = int(input("Podaj liczbę kolumn 2 macierzy: "))

def multiply_matrices(m1_rows, m1_cols, m2_rows, m2_cols):
    multiple_matrix = []
    for i in range(len(m1_cols)):
        new_row = []
        for j in range(len(m1_rows)):
            new_row.append(m1_cols[i][j] * m2_cols[i][j])
        multiple_matrix.append(new_row)
    return multiple_matrix


if rows_number_1 == rows_number_2 and columns_number_1 == columns_number_2:
    matrices = []
    columns_1 = []
    for _ in range(1, columns_number_1 + 1):
        rows_1 = []
        for _ in range(1, rows_number_1 + 1):
            rows_1.append(randrange(5))
        columns_1.append(rows_1)
    matrices.append(columns_1)

    columns_2 = []
    for _ in range(1, columns_number_2 + 1):
        rows_2 = []
        for _ in range(1, rows_number_2 + 1):
            rows_2.append(randrange(5))
        columns_2.append(rows_2)
    matrices.append(columns_2)

    print(matrices[0])
    print(matrices[1])
    print(multiply_matrices(rows_1, columns_1, rows_2, columns_2))
else:
    print("Uruchom program ponownie i podaj macierze, które można dodać lub odjąć")
    exit()

