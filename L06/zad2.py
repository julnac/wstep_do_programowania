number_1 = int(input("Podaj pierwszą liczbę: "))
number_2 = int(input("Podaj drugą liczbę: "))

max_multiple = number_1 * number_2
multiple_set_1 = set()
multiple_set_2 = set()

for x in range(1, number_2 + 1):
    multiple_set_1.add(number_1 * x)
for y in range(1, number_1 + 1):
    multiple_set_2.add(number_2 * y)

common_multiples = multiple_set_1.intersection(multiple_set_2)

print(f"NWW liczb {number_1} i {number_2} to {min(common_multiples)}.")
