n = int(input("Podaj liczbę od 0 do 10: "))
main_list = []

for x in range(1, n + 1):
    inner_list = []
    for y in range(1, n + 1):
        inner_list.append(x * y)
    main_list.append(inner_list)

for element in main_list:
    print(element)
