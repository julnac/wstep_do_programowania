a = int(input("Podaj liczbe: "))
b = int(input("Podaj liczbe: "))
c = int(input("Podaj liczbe: "))

if a == b:
    if b == c:
        print("Wszystkie liczby są równe.")
    else:
        print("Liczby a i b są równe.")
elif a == c:
    if c == b:
        print("Wszystkie liczby są równe.")
    else:
        print("Liczby a i c są równe.")
elif b == c:
    if a == c:
        print("Wszystkie liczby są równe.")
    else:
        print("Liczby b i c są równe.")
else:
    print("Nie ma pary równych liczb.")