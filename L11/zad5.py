import numpy as np
import matplotlib.pyplot as plt

def data_from_file(file_path):
    try:
        dane = []
        with open(file_path, 'r') as file:
            for line in file:
                dane.append(line)
        return dane
    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except ValueError:
        print("The file contains non-numeric data.")


file = 'wynikiKolokwium.txt'
dane = data_from_file(file)
oceny = [" ".join(x.split()[:-1]) for x in dane]
liczby = [int(x.split()[-1]) for x in dane]

suma = sum(liczby)
procenty = [x / suma * 100 for x in liczby]

plt.figure(figsize=(8, 8))
plt.pie(procenty, labels=oceny, autopct='%1.1f%%', startangle=140)
plt.title("Wyniki kolokwium")
plt.show()
