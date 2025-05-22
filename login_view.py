import tkinter as tk
from services.mi_sql import conectar

def cargar_login(ventana):
    login_panel = tk.Frame(
        ventana,
        bg="purple",
        width=1000,
        height=600,
    )
    login_panel.pack()

    # ===== LOGIN =====
    título = tk.Label(login_panel, text="Login", bg="purple", fg="white", font=("Arial", 16))
    título.grid(row=0, column=0, columnspan=2, pady=10)

    tk.Label(login_panel, text="Correo:", bg="purple", fg="white").grid(row=1, column=0, sticky="e", padx=5, pady=5)
    entrada_correo = tk.Entry(login_panel)
    entrada_correo.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(login_panel, text="Contraseña:", bg="purple", fg="white").grid(row=2, column=0, sticky="e", padx=5, pady=5)
    entrada_contrasenna = tk.Entry(login_panel, show="*")
    entrada_contrasenna.grid(row=2, column=1, padx=5, pady=5)

    # ===== ÁREA DE TEXTO PARA MOSTRAR CATEGORÍAS =====
    cuadro_categorias = tk.Text(login_panel, width=40, height=15)
    cuadro_categorias.grid(row=0, column=3, rowspan=6, padx=20, pady=10)

    # ===== BOTÓN INGRESAR =====
    def funcion_boton():
        correo = entrada_correo.get()
        contrasenna = entrada_contrasenna.get()

        categorias = conectar("SELECT * FROM categorias")
        cuadro_categorias.delete("1.0", tk.END)

        if categorias:
            for fila in categorias:
                cuadro_categorias.insert(tk.END, f"{fila[0]} - {fila[1]}\n")
        else:
            cuadro_categorias.insert(tk.END, "No se encontraron categorías.")

    tk.Button(login_panel, text="Continuar", command=funcion_boton).grid(row=3, column=0, columnspan=2, pady=10)
