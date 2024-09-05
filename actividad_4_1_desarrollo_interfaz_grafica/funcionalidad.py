import tkinter as tk
import tkinter.messagebox as messagebox

def agregar_tarea(entrada, lista):
    tarea = entrada.get()
    if tarea:
        lista.insert(tk.END, tarea)
        entrada.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingrese una tarea.")

def eliminar_tarea(lista):
    try:
        seleccion = lista.curselection()[0]
        lista.delete(seleccion)
    except IndexError:
        messagebox.showwarning("Advertencia", "Seleccione una tarea para eliminar.")

def marcar_como_completada(lista):
    try:
        seleccion = lista.curselection()[0]
        tarea = lista.get(seleccion)
        # Aquí puedes definir el estilo para las tareas completadas
        lista.itemconfig(seleccion, {'bg':'#d3ffd3', 'fg':'#808080'})  # Fondo verde claro y texto gris
    except IndexError:
        messagebox.showwarning("Advertencia", "Seleccione una tarea para marcar como completada.")
