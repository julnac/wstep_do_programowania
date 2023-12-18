w1_str = input("Podaj pierwszy wektor: ")
w2_str = input("Podaj drugi wektor: ")

wektor_1 = w1_str.split(' ')
wektor_2 = w2_str.split(' ')

wektor_1 = [int(w) for w in wektor_1 if w != '']
wektor_2 = [int(w) for w in wektor_2 if w != '']
iloczyn = sum([w1*w2 for w1, w2 in zip(wektor_1, wektor_2)])

print(iloczyn)
