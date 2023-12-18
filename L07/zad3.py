import string

alphabet = string.ascii_lowercase
alphabet_list = []
for x in alphabet:
    alphabet_list.append(x)


def encrypt_cezar(number, word):
    cezar_list = []
    for y in word:
        index = alphabet_list.index(y)
        new_index = index + number
        cezar_list.append(alphabet_list[new_index])

    cezar = ""
    for ele in cezar_list:
        cezar += ele
    return cezar


if __name__ == "__main__":
    user_number = int(input("Podaj liczbę: "))
    user_word = input("Podaj wyraz do zaszyfrowania: ")
    print(encrypt_cezar(user_number, user_word))
