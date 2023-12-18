print("1.Dodawanie\n2.Odejmowanie\n3.Mnożenie")
w = int(input('Wybierz działanie: '))

if w == 1:
    a = int(input("Podaj liczbe a: "))
    b = int(input("Podaj liczbe b: "))
    print(a+b)
elif w == 2:
    a = int(input("Podaj liczbe a: "))
    b = int(input("Podaj liczbe b: "))
    print(a - b)
elif w == 2:
    a = int(input("Podaj liczbe a: "))
    b = int(input("Podaj liczbe b: "))
    print(a * b)