a = int(input("Podaj liczbe: "))
b = int(input("Podaj liczbe: "))
c = int(input("Podaj liczbe: "))

if a == b and b !=c:
    print("Liczby a i b są równe.")
elif a == c and c != b:
    print("Liczby a i c są równe.")
elif b == c and c != a:
    print("Liczby b i c są równe.")
elif a == b == c:
    print("Wszystkie liczby są równe.")
else:
    print("Nie ma pary równych liczb.")