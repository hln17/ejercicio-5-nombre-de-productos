# views/productos_view.py

import tkinter as tk
from services.mi_sql import conectar

def cargar_productos(ventana):
    productos_panel = tk.Frame(
        ventana,
        bg="pink",
        width=1000,
        height=540,
    )
    productos_panel.pack()

    # Cuadro de texto para mostrar los datos
    texto_resultado = tk.Text(productos_panel, width=100, height=25)
    texto_resultado.pack(pady=10)

    # Ejecutar consulta y obtener datos
    datos = conectar("SELECT * FROM categorias")

    # Mostrar los datos en el cuadro de texto
    if datos:
        for fila in datos:
            texto_resultado.insert(tk.END, f"ID: {fila[0]}  |  Nombre: {fila[1]}\n")
    else:
        texto_resultado.insert(tk.END, "No se encontraron categorías.")


