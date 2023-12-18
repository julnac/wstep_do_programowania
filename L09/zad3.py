def sel_sort(list):
    for x in range(0, len(list)):
        minimal_index = x
        for y in range(x, len(list)):
            if list[y] < list[minimal_index]:
                minimal_index = y

        list[x], list[minimal_index] = list[minimal_index], list[x]

    return list


n = int(input("Podaj długość listy: "))
lista = []

for _ in range(n):
    m = input("Podaj liczbe całkowitą: ")
    lista.append(m)

print(sel_sort(lista))