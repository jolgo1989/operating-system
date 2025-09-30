# src/gui/explorador/listar.py

import tkinter as tk
import os
from src.config import config_boton 

CARPETA = os.path.expanduser('~')  # Directorio home del usuario

def crear_ventana_explorador():
    ventana = tk.Toplevel()
    ventana.title("Listado de Archivos")
    ventana.geometry("600x400")

    lista = tk.Listbox(ventana, width=60, height=15)
    lista.pack(pady=10)

    def listar_archivos():
        lista.delete(0, tk.END)
        try:
            archivos = os.listdir(CARPETA)
            if archivos:
                for archivo in archivos:
                    lista.insert(tk.END, archivo)
            else:
                lista.insert(tk.END, "La carpeta está vacía.")
        except Exception as e:
            lista.insert(tk.END, f"Error: {e}")

    btn_listar = tk.Button(ventana, text="Listar archivos", command=listar_archivos, **config_boton)
    btn_listar.pack(pady=10)