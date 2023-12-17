# https://aprendeconalf.es/docencia/python/manual/matplotlib/

import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Función para limpiar el mensaje de error
def limpiar_error():
    etiqueta_error.config(text="")

# Función para actualizar el mensaje de error y limpiarlo después de 5 segundos
def actualizar_error(mensaje):
    etiqueta_error.config(text=mensaje)
    # Limpia el mensaje después de 5000 ms (5 segundos)
    ventana.after(5000, limpiar_error)  

# Función para validar y convertir las entradas de temperatura
def temperaturas(entrada):
    try:
        # Convierte la entrada en una lista de floats
        return list(map(float, entrada.split(',')))
    except ValueError:
        raise ValueError("Ingresar 7 números separados por comas.")

# Función para dibujar la gráfica
def dibujar_grafica():
    try:
        temperaturas_madrid = temperaturas(entrada_madrid.get())
        temperaturas_barcelona = temperaturas(entrada_barcelona.get())

        if len(temperaturas_madrid) != 7 or len(temperaturas_barcelona) != 7:
            raise ValueError("Debe ingresar 7 temperaturas para cada ciudad.")

        fig, ax = plt.subplots()
        dias = ['L', 'M', 'X', 'J', 'V', 'S', 'D']
        ax.plot(dias, temperaturas_madrid, label='Madrid')
        ax.plot(dias, temperaturas_barcelona, label='Barcelona')
        ax.legend(loc='upper right')
        ax.set_title("Gráfica básica del tiempo")

        canvas = FigureCanvasTkAgg(fig, master=ventana)  
        widget_canvas = canvas.get_tk_widget()
        widget_canvas.grid(row=3, column=0, columnspan=4)

        actualizar_error("")  # Limpia cualquier mensaje de error anterior

    except ValueError as e:
        actualizar_error(str(e))

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Temperaturas de Madrid y Barcelona")

etiqueta_madrid = tk.Label(ventana, text=" Introduce 7 Temperaturas para Madrid (separadas por comas):")
etiqueta_madrid.grid(row=0, column=0, sticky="w")
entrada_madrid = tk.Entry(ventana)
entrada_madrid.grid(row=0, column=1)

etiqueta_barcelona = tk.Label(ventana, text="Introduce 7 Temperaturas para Barcelona (separadas por comas):")
etiqueta_barcelona.grid(row=1, column=0, sticky="w")
entrada_barcelona = tk.Entry(ventana)
entrada_barcelona.grid(row=1, column=1)

boton_dibujar = tk.Button(ventana, text="Dibujar gráfica", command=dibujar_grafica)
boton_dibujar.grid(row=2, column=0, columnspan=2)

etiqueta_error = tk.Label(ventana, text="", fg="red")
etiqueta_error.grid(row=2, column=2, columnspan=2)

ventana.mainloop()



