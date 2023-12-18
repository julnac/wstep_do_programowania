def dwumian(n, k):
    if k == 0 or k == n:
        return 1
    return dwumian(n - 1, k - 1) + dwumian(n - 1, k)


def prawdopodobieństwo(n, m):
        return dwumian(n, m) * (0.5 ** m) * ((1 - 0.5) ** (n - m))


if __name__ == "__main__":
    n = int(input("podaj liczbe rzutów:\n"))
    m = int(input("podaj liczbe orłów:\n"))
    print(prawdopodobieństwo(n, m))