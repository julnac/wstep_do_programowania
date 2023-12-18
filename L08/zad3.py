def reverse(napis):
    dl = len(napis)
    if dl == 0:
        return ""
    else:
        return napis[-1] + reverse(napis[:-1])


if __name__ == "__main__":
    napis = input("Podaj napis: ")
    print(reverse(napis))
