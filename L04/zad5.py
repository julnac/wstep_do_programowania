napis = input("Podaj dowolne zdanie: ")
slowa = 1
for x in napis:
    if x == " ":
        slowa += 1

print(slowa)