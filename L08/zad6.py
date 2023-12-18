def binar(n):
    if n == 0:
        return ""
    return binar(n // 2) + str(n % 2)


if __name__ == "__main__":
    n = int(input("Podaj n: "))
    print(binar(n))