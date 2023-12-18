def sort(list):
    for y in range(len(list) - 1):
        if list[y] > list[y + 1]:
            pam = list[y]
            list[y] = list[y + 1]
            list[y + 1] = pam
    return list


n = int(input("Podaj długość listy: "))
lista = []

for _ in range(n):
    m = input("Podaj liczbe całkowitą: ")
    lista.append(m)

print(sort(lista))
