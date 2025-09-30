import tkinter as tk
from src.gui.explorer import crear_ventana_explorador
from src.config.styles import config_boton

def lanzar_menu_principal():
    root = tk.Tk()
    root.title("Mini Sistema Operativo Educativo")
    root.geometry("400x400")
    root.configure(bg="#f0f0f0")

    tk.Label(root, text="Menú Principal", font=("Arial", 16), bg="#f0f0f0").pack(pady=20)

    tk.Button(root, text="📂 Explorador de Archivos", command=crear_ventana_explorador, **config_boton).pack(pady=10)

    root.mainloop()