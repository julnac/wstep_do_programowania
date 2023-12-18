def potega(n, a):
    if n == 0:
        return 1
    else:
        return a * potega(n - 1, a)


if __name__ == "__main__":
    a = int(input("Podaj a: "))
    n = int(input("Podaj n: "))
    print(potega(n, a))
