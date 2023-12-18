napis = input("Podaj dowolne zdanie: ")

samo = 0

for x in napis:
    if x in "aeiouy":
        samo += 1
    
print(samo)