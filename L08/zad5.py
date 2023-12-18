def dwumian(n, k):
    if k == 0 or k == n:
        return 1
    return dwumian(n - 1, k - 1) + dwumian(n - 1, k)


if __name__ == "__main__":
    n = int(input("Podaj n: "))
    k = int(input("Podaj k: "))
    print(dwumian(n, k))