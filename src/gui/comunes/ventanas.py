# src/gui/comunes/ventanas.py
import tkinter as tk

def crear_ventana_secundaria(titulo="Ventana"):
    ventana = tk.Toplevel()
    ventana.title(titulo)
    ventana.geometry("600x400")
    return ventana
