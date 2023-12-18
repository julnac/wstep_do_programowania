import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

y_sin = np.sin(x)
y_cos = np.cos(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y_sin, label='sin(x)', color='blue')
plt.plot(x, y_cos, label='cos(x)', color='red')

plt.xticks(np.arange(-2 * np.pi, 2.5 * np.pi, np.pi / 2),
           ['-2π', '-3π/2', '-π', '-π/2', '0', 'π/2', 'π', '3π/2', '2π'])
plt.yticks([-1, 0, 1], ['-1', '0', '1'])
plt.title('Wykres funkcji sinus i cosinus')
plt.xlabel('Oś X')
plt.ylabel('Oś Y')
plt.legend()
plt.show()
