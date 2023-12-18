import numpy as np

def add(x, y):
    return np.add(x, y)

def subtract(x, y):
    return np.subtract(x, y)

def multiply(x, y):
    return np.multiply(x, y)

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return np.divide(x, y)

def modulo(x, n):
    return np.mod(x, n)

def power(x, y):
    return np.power(x, y)

def sqrt(x):
    return np.sqrt(x)

def factorial(n):
    return np.math.factorial(n)

def logarithm(base, x):
    return np.log(x) / np.log(base)

def sin(x):
    return np.sin(np.radians(x))

def cos(x):
    return np.cos(np.radians(x))

def tan(x):
    return np.tan(np.radians(x))

def cot(x):
    return 1 / np.tan(np.radians(x))

def main():
    while True:
        print("\nRozbudowany kalkulator:")
        print("1. Dodawanie")
        print("2. Odejmowanie")
        print("3. Mnożenie")
        print("4. Dzielenie")
        print("5. Modulo")
        print("6. Potęgowanie")
        print("7. Pierwiastkowanie")
        print("8. Silnia")
        print("9. Logarytmowanie")
        print("10. Sinus")
        print("11. Cosinus")
        print("12. Tangens")
        print("13. Cotangens")
        print("14. Wyjście")

        choice = input("Wybierz operację (1-14): ")

        if choice == '14':
            break

        if choice in ['1', '2', '3', '4', '5', '6', '9']:
            x = float(input("Podaj pierwszą liczbę: "))
            y = float(input("Podaj drugą liczbę: "))

        elif choice in ['7', '10', '11', '12', '13']:
            x = float(input("Podaj liczbę: "))

        elif choice == '8':
            n = int(input("Podaj liczbę całkowitą (n): "))

        if choice == '1':
            print("Wynik: ", add(x, y))
        elif choice == '2':
            print("Wynik: ", subtract(x, y))
        elif choice == '3':
            print("Wynik: ", multiply(x, y))
        elif choice == '4':
            print("Wynik: ", divide(x, y))
        elif choice == '5':
            print("Wynik: ", modulo(x, y))
        elif choice == '6':
            print("Wynik: ", power(x, y))
        elif choice == '7':
            print("Wynik: ", sqrt(x))
        elif choice == '8':
            print("Wynik: ", factorial(n))
        elif choice == '9':
            print("Wynik: ", logarithm(y, x))
        elif choice == '10':
            print("Wynik: ", sin(x))
        elif choice == '11':
            print("Wynik: ", cos(x))
        elif choice == '12':
            print("Wynik: ", tan(x))
        elif choice == '13':
            print("Wynik: ", cot(x))
        else:
            print("Nieprawidłowy wybór")

if __name__ == "__main__":
    main()
