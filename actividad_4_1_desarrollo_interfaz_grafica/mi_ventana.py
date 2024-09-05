import tkinter as tk

# Crear una instancia de la ventana principal
ventana = tk.Tk()
ventana.title("Mi Ventana Tkinter")
ventana.geometry("300x200")

# Crear un widget de etiqueta
etiqueta = tk.Label(ventana, text="¡Hola, Tkinter!")
etiqueta.pack(pady=20)

# Crear un botón
boton = tk.Button(ventana, text="Haz clic aquí", command=lambda: etiqueta.config(text="¡Botón clickeado!"))
boton.pack(pady=10)

# Ejecutar el bucle principal de la aplicación
ventana.mainloop()
