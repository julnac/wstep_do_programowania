import numpy as np
import matplotlib.pyplot as plt

n = int(input("Podaj n: "))
p = float(input("Podaj p: "))
s = int(input("Podaj s: "))

eagle_count = 0

for i in range(s):
    for j in range(n):
        if p > np.random.random():
            eagle_count += 1

all_throws = n * s
dist = [eagle_count/all_throws, (all_throws - eagle_count) / all_throws]

x = [0, 1]

plt.figure(figsize=(10, 6))
plt.bar(x, dist)

plt.title('Rzut monetą')
plt.legend()
plt.show()
