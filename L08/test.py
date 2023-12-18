def suma(n):
    numbers_sum = 0
    while n != 0:
        numbers_sum += n % 10
        n //= 10
    return numbers_sum


if __name__ == "__main__":
    n = int(input("podaj liczbe:\n"))
    print(suma(n))
