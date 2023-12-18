def find_bin(zbior, target, start, end):
    if start > end:
        return print("Nie istnieje")

    middle_index = (start + end) // 2

    if zbior[middle_index] == target:
        return middle_index
    if zbior[middle_index] > target:
        return find_bin(zbior, target, start, middle_index - 1)
    if zbior[middle_index] < target:
        return find_bin(zbior, target, middle_index + 1, end)


n = int(input("Podaj szukany element: "))
lista = [1, 2, 5, 6, 8, 10, 27, 56, 73, 100]

print(find_bin(lista, n, 0, len(lista)))