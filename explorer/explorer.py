import tkinter as tk
import subprocess
import platform
import os

# Carpeta que quieres listar (home de WSL)
CARPETA = os.path.expanduser('~')  # Directorio home del usuario en WSL
# CARPETA = r'/mnt/d'  # Directorio home del usuario en WSL

# Crear ventana principal
root = tk.Tk()
root.title("Listado de Archivos")
root.geometry("1100x400")

# Caja de texto donde se mostrarán los archivos
lista = tk.Listbox(root, width=50, height=15)
lista.pack(pady=10)

#? Función para listar archivos
def listar_archivos():
    lista.delete(0, tk.END)  # Cambio: usar 0 en lugar de "1.0"
    try:
        archivos = os.listdir(CARPETA)
        if archivos:
            for archivo in archivos:
                lista.insert(tk.END, archivo)  # Cambio: quitar el "\n"
        else:
            lista.insert(tk.END, "La carpeta está vacía.")
    except Exception as e:
        lista.insert(tk.END, f"Error: {e}")

#? Función para abrir la carpeta seleccionada
#? Función para navegar a la carpeta seleccionada (CAMBIO PRINCIPAL: Ya no abre explorador externo)
def abrir_carpeta():
    global CARPETA  # CAMBIO: Declarar CARPETA como global para modificarla
    try:
        # Obtener el índice del elemento seleccionado
        seleccion = lista.curselection()
        if not seleccion:
            lista.insert(tk.END, "Error: Selecciona una carpeta primero")
            return
        
        # Obtener el nombre de la carpeta seleccionada
        carpeta_seleccionada = lista.get(seleccion[0])
        ruta_completa = os.path.join(CARPETA, carpeta_seleccionada)
        
        # Verificar si es una carpeta
        if not os.path.isdir(ruta_completa):
            lista.insert(tk.END, f"Error: '{carpeta_seleccionada}' no es una carpeta")
            return
        
        # CAMBIO PRINCIPAL: En lugar de abrir explorador externo, cambiar la carpeta actual
        CARPETA = ruta_completa
        
        # CAMBIO: Actualizar el título de la ventana con la nueva ruta
        root.title(f"Listado de Archivos - {CARPETA}")
        
        # CAMBIO: Llamar automáticamente a listar_archivos para mostrar el contenido
        listar_archivos()
        
        # ELIMINAR: Todo el código de subprocess que abría explorador externo
            
    except Exception as e:
        lista.insert(tk.END, f"Error al navegar: {e}")

#? Función para volver a la carpeta anterior
def volver_atras():
    global CARPETA
    try:
        # Obtener la carpeta padre
        carpeta_padre = os.path.dirname(CARPETA)
        
        # Verificar que no estemos en la raíz del sistema
        if carpeta_padre != CARPETA:  # Evita bucle infinito en la raíz
            CARPETA = carpeta_padre
            
            # Actualizar el título de la ventana
            root.title(f"Listado de Archivos - {CARPETA}")
            
            # Mostrar el contenido de la carpeta padre
            listar_archivos()
        else:
            lista.insert(tk.END, "Ya estás en la carpeta raíz")
            
    except Exception as e:
        lista.insert(tk.END, f"Error al volver: {e}")


# Configuración común de botones
config_boton = {
    "bg": "#006A67",
    "fg": "white",
    "font": ("Arial", 12),
    "padx": 20,
    "pady": 10,
    "cursor": "hand2"
}

# Contenedor para los botones
frame_botones = tk.Frame(root)
frame_botones.pack(pady=10)

# Crear botones con configuración común
boton_volver = tk.Button(frame_botones, text="← Volver", command=volver_atras, **config_boton)
boton_listar = tk.Button(frame_botones, text="Listar Archivos", command=listar_archivos, **config_boton)
boton_cambiar = tk.Button(frame_botones, text="Cambiar Carpeta", **config_boton)
boton_crear = tk.Button(frame_botones, text="Crear carpeta", **config_boton)
boton_eliminar = tk.Button(frame_botones, text="Eliminar carpeta", **config_boton)
boton_abrir = tk.Button(frame_botones, text="Abrir archivo",command=abrir_carpeta, **config_boton)


# Posicionar botones
boton_volver.grid(row=0, column=0, padx=5, pady=5)
boton_listar.grid(row=0, column=1, padx=10, pady=5)
boton_abrir.grid(row=0, column=2, padx=5, pady=5)
boton_crear.grid(row=1, column=0, padx=5, pady=5)
boton_cambiar.grid(row=1, column=1, padx=15, pady=5)
boton_eliminar.grid(row=1, column=2, padx=20, pady=5)


root.mainloop()