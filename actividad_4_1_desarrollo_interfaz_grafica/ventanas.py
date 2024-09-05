import tkinter as tk
from funcionalidad import agregar_tarea, eliminar_tarea, marcar_como_completada

class VentanaPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")
        self.root.geometry("300x250")
        self.root.configure(bg="#f0f8ff")  # Color de fondo de la ventana
        
        # Crear widgets
        self.entrada_tarea = tk.Entry(root, width=40, font=('Arial', 14))
        self.entrada_tarea.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        self.boton_agregar = tk.Button(root, text="Agregar Tarea", command=self.agregar_tarea, bg="#add8e6", fg="black", font=('Arial', 12, 'bold'))
        self.boton_agregar.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

        self.boton_eliminar = tk.Button(root, text="Eliminar Tarea", command=self.eliminar_tarea, bg="#add8e6", fg="black", font=('Arial', 12, 'bold'))
        self.boton_eliminar.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        self.boton_completar = tk.Button(root, text="Marcar como Completada", command=self.marcar_como_completada, bg="#add8e6", fg="black", font=('Arial', 12, 'bold'))
        self.boton_completar.grid(row=1, column=2, padx=10, pady=5, sticky="ew")

        self.lista_tareas = tk.Listbox(root, width=60, height=10, bg="#ffffe0", font=('Arial', 12), selectmode=tk.SINGLE)
        self.lista_tareas.grid(row=2, column=0, columnspan=3, padx=10, pady=10)
        
        # Configurar la expansión de columnas y filas
        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=1)
        root.grid_columnconfigure(2, weight=1)
        root.grid_rowconfigure(2, weight=1)

    def agregar_tarea(self):
        agregar_tarea(self.entrada_tarea, self.lista_tareas)
        
    def eliminar_tarea(self):
        eliminar_tarea(self.lista_tareas)

    def marcar_como_completada(self):
        marcar_como_completada(self.lista_tareas)
