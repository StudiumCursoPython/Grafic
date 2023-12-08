import tkinter as tk
from tkinter import ttk, PhotoImage
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os, sys

# Función para actualizar el gráfico y la etiqueta del valor
def update_graph(val):
    val_float = float(val)
    y = price_data + val_float * np.sin(x)
    line.set_ydata(y)
    canvas.draw()
    label_valor.config(text=f'Amplitud: {val_float:.2f}')

# Datos de precios simulados (puedes cargar tus propios datos aquí)
# Supongamos que estos son los datos de un índice de precios a lo largo de un período de tiempo.
x = np.linspace(0, 24, 100)
price_data = 100 + 5 * np.random.randn(100)  # Índice de precios inicial de 100 con variabilidad aleatoria

# Ventana de Tkinter
aplicacion = tk.Tk()
aplicacion.title("Ajuste de amplitud de datos de un índice de precios")

# (Resto del código es similar al proporcionado en la pregunta)

# Obtener la ruta de acceso a los recursos incluidos en el archivo
ruta_recursos = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

# Crear la ventana de la aplicación
icono = PhotoImage(file=os.path.join(ruta_recursos, "Studium.png"))

# Creación del marco para el gráfico y el slider
frame = tk.Frame(aplicacion)
frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Creación de la figura de Matplotlib
fig, ax = plt.subplots(figsize=(10, 6))
line, = ax.plot(x, price_data, label='Índice de Precios')
ax.set_title('Índice de Precios a lo largo del Tiempo')
ax.set_xlabel('Tiempo')
ax.set_ylabel('Índice de Precios')
ax.legend()
ax.grid(True)

# Poner la figura en Tkinter en el marco
canvas = FigureCanvasTkAgg(fig, master=frame)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Creación del marco para el slider y la etiqueta
slider_frame = tk.Frame(aplicacion)
slider_frame.pack(side=tk.RIGHT, fill=tk.Y)

# Creación de la etiqueta para mostrar el valor del slider
label_valor = tk.Label(slider_frame, text='Amplitud: 1.00')
label_valor.pack()

# Creación del slider
slider = ttk.Scale(slider_frame, from_=0.1, to=10.0, orient='vertical', command=update_graph)
# Establecer valor inicial
slider.set(1.0)
slider.pack()

# Inicio de interfaz Tkinter
aplicacion.iconphoto(True, icono)
aplicacion.mainloop()




