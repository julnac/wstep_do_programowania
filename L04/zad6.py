def get_length():
    length = 0
    for _ in text:
        length += 1
    return length


def generate_substrings():
    for start in range(0, text_length):
        for end in range(start + 1, text_length + 1):
            print(f"{text[start:end]}")


if __name__ == "__main__":
    text = input("Podaj ciag znaków: ")
    text_length = get_length()
    generate_substrings()
