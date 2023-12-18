import numpy as np


def find_possible_matrices(array):
    n = array.size
    mat_array = []
    for i in range(1, n + 1):
        if n % i == 0:
            mat_array.append(array.reshape(i, n // i))

    return mat_array


def main():
    n = int(input("Podaj rozmiar tablicy (n): "))
    np_array = np.zeros(n, dtype=int)
    for i in range(len(np_array)):
        inp = int(input("Podaj wartość: "))
        np_array[i] = inp

    print("Oryginalna tablica: ", np_array)

    print("\nWszystkie możliwe macierze:")
    for matrix in find_possible_matrices(np_array):
        print(matrix)


if __name__ == "__main__":
    main()