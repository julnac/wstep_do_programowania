def ins_sort(input_numbers):
    for x in range(1, len(input_numbers)):
        pam = input_numbers[x]
        while x > 0 and input_numbers[x - 1] > input_numbers[x]:
            input_numbers[x] = input_numbers[x - 1]
            input_numbers[x - 1] = pam
            x = x - 1
    return input_numbers


n = int(input("Podaj długość listy: "))
lista = []

for _ in range(n):
    m = input("Podaj liczbe całkowitą: ")
    lista.append(m)

print(ins_sort(lista))
