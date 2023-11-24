import matplotlib.pyplot as plt
import numpy as np

# https://aprendeconalf.es/docencia/python/manual/matplotlib/
# Datos 
x = np.linspace(0, 5, 100)
y = np.sin(x)

# Crear la gráfica
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='sin(x)')
plt.title('Gráfica Básica de sin(x)')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.legend()
plt.grid(True)
plt.show()
