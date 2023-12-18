n = int(input("Podaj liczbę naturalną n: "))

for i in range(n):
    for j in range(n):
        print("1" if j % 2 == 0 else "0", end=" ")
    print()

