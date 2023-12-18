z = input("Podaj dowolne zdanie: ")

z = z.lower().replace(" ","")

if z.endswith("."):
    z = z[0:-1]

for x in range(0,len(z)//2):
    if z[x] != z[-x - 1]:
        print("Zdanie nie jest  palindromem.")
        break
else:
    print("Zdanie jest  palindromem.")
