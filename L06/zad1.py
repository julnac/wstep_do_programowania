import math
import numpy as np

LOWER_LIMIT = 1
UPPER_LIMIT = 1000

n = int(input("Podaj liczbę od 1 do 1000: "))
pierwiastek_n = int(math.sqrt(n))

if UPPER_LIMIT >= n >= LOWER_LIMIT:
    myset = np.arange(1, n+1)
else:
    exit()

numbers_to_preserve = [True] * n

for i in range(2, pierwiastek_n + 1):
    for j in myset:
        if j != i and j % i == 0:
            numbers_to_preserve[j-1] = False

prime_numbers_set = set()

for j, should_preserve in enumerate(numbers_to_preserve):
    if should_preserve:
        prime_numbers_set.add(j + 1)

print(prime_numbers_set)
