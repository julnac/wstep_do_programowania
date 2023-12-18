from random import randrange


def generate_matrix():
    rows_number = int(input("Podaj liczbę wierszy: "))
    columns_number = int(input("Podaj liczbę kolumn: "))
    columns = []
    for x in range(1, columns_number + 1):
        rows = []
        for y in range(1, rows_number + 1):
            rows.append(randrange(5))
        columns.append(rows)
    return columns


def add_matrix(matrix_1, matrix_2):
    sum_matrix = []
    for i in range(len(matrix_1)):
        new_row = []
        for j in range(len(matrix_1[0])):
            new_row.append(matrix_1[i][j] + matrix_2[i][j])
        sum_matrix.append(new_row)
    return sum_matrix


def subtract_matrix(matrix_1, matrix_2):
    difference_matrix = []
    for i in range(len(matrix_1)):
        new_row = []
        for j in range(len(matrix_1[0])):
            new_row.append(matrix_1[i][j] - matrix_2[i][j])
        difference_matrix.append(new_row)
    return difference_matrix


def check_if_matrices_sizes_match(matrix_1, matrix_2):

    if len(matrix_1) == len(matrix_2) and len(matrix_1[0]) == len(matrix_2[0]):
        return True

    return False


if __name__ == "__main__":

    first_matrix = generate_matrix()
    second_matrix = generate_matrix()
    if check_if_matrices_sizes_match(first_matrix, second_matrix):
        print(f"Pierwsza macierz: {first_matrix}")
        print(f"Druga macierz: {second_matrix}")

    else:
        print("Uruchom program ponownie i podaj macierze, które można dodać lub odjąć")
        exit()

    print(f"Dodawanie: {add_matrix(first_matrix, second_matrix)}")
    print(f"Odejmowanie: {subtract_matrix(first_matrix, second_matrix)}")

