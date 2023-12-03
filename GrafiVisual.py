"""
Curso Python empresa

Autor: José Antonio Calvo López
Fecha: Noviembre de 2023
"""

import tkinter as tk
from tkinter import ttk,PhotoImage
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os, sys

# https://aprendeconalf.es/docencia/python/manual/matplotlib/

# Función para actualizar el gráfico y la etiqueta del valor
def update_graph(val):
    val_float = float(val)
    y = np.sin(x * val_float)
    line.set_ydata(y)
    canvas.draw()
    label_valor.config(text=f'Valor: {val_float:.2f}')

# Ventana de Tkinter
aplicacion = tk.Tk()
aplicacion.title("Slider para ajustar sin(x)")

# Obtener la ruta de acceso a los recursos incluidos en el archivo
ruta_recursos = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

# Crear la ventana de la aplicación
icono = PhotoImage(file=os.path.join(ruta_recursos, "Studium.png"))

# Creación del marco para el gráfico y el slider
frame = tk.Frame(aplicacion)
frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Creación de la figura de Matplotlib
fig, ax = plt.subplots(figsize=(10, 6))
x = np.linspace(0, 5, 100)
y = np.sin(x)
line, = ax.plot(x, y, label='sin(x)')
ax.set_title('Gráfica Básica de sin(x)')
ax.set_xlabel('x')
ax.set_ylabel('sin(x)')
ax.legend()
ax.grid(True)

# Poner la figura a Tkinter en el marco
canvas = FigureCanvasTkAgg(fig, master=frame)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Creación del marco para el slider y la etiqueta
slider_frame = tk.Frame(aplicacion)
slider_frame.pack(side=tk.RIGHT, fill=tk.Y)

# Creación de la etiqueta para mostrar el valor del slider
label_valor = tk.Label(slider_frame, text='Valor: 1.00')
label_valor.pack()

# Creación del slider
slider = ttk.Scale(slider_frame, from_=0.5, to=2.0, orient='vertical', command=update_graph)
# Establecer valor inicial
slider.set(1)  
slider.pack()

# Inicio de interfaz Tkinter
aplicacion.iconphoto(True, icono)
aplicacion.mainloop()

