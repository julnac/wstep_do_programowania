def suma(n):
    if n == 0:
        return 0
    else:
        return n % 10 + suma(n // 10)

if __name__ == "__main__":
    n = int(input("podaj liczbe:\n"))
    print(suma(n))