names = (("Einstein", "Albert"), ("Bohr", "Niels"), ("Oppenheimer", "Robert"), ("Newton", "Isaac"), ("Turing", "Alan"))

input_surname = input("Podaj nazwisko: ")

for surname, name in names:
    if input_surname == surname:
        print(f'{name}')
        break
