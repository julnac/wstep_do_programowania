num_elements = int(input("Podaj ilość elementów w zbiorze: "))
user_set = set()

for _ in range(num_elements):
    element = input("Podaj nowy element (liczba, znak, łańcuch znaków): ")
    user_set.add(element)

print(user_set)
all_subsets = []

elements = list(user_set)
n = len(elements)

for i in range(2**n):
    subset = []
    for j in range(n):
        if i & (1 << j):
            subset.append(elements[j])
    all_subsets.append(subset)

print("Wszystkie podzbiory zbioru:")
for subset in all_subsets:
    print(subset)



