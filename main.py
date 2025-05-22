import tkinter as tk 
from views.header_view import cargar_header
from views.productos_view import cargar_productos
from views.login_view import cargar_login


#VENTANA DE LA APLICACIÓN
ventana = tk.Tk()
ventana.title("mi tienda")
ventana.geometry("1000x600")

#MÓDULOS DE LA VENTANA
cargar_login(ventana)

ventana.mainloop()

