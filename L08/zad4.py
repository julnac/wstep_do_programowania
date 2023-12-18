def fib(n):
    if n < 3:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    n = int(input("Podaj n: "))
    print(fib(n))