z = input("Podaj dowolne zdanie: ")

if z[0].islower() or z[-1] != '.':
    print("Zdanie jest niepoprawne")
else:
    print("Zdanie jest poprawne")