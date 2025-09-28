import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk


# # Crear la ventana principal
root = tk.Tk()

# # Configurar la ventana
root.title("Mi Primera Aplicación")
root.geometry("600x400")  # Ancho x Alto
root.configure(bg="#0A0A23")  # Color de fondo


#?Función para abrir nueva ventana
def abrir_nueva_ventana():
    nueva_ventana = tk.Toplevel(root)
    nueva_ventana.title("Nueva Ventana")
    nueva_ventana.geometry("400x300")
    nueva_ventana.configure(bg="#0A0A23" )
    
    
    list_img = Image.open("./list.png")
    list_img_redimencionada = list_img.resize((64, 64))
    list_img_tk = ImageTk.PhotoImage(list_img_redimencionada)

    # Contenido de la nueva ventana
    label_contenido = tk.Label(nueva_ventana, text="¡Has abierto una nueva ventana!", 
                              font=("Arial", 14), bg="#f0f0f0",image=list_img_tk )
    label_contenido.image = list_img_tk  # Mantener referencia
    label_contenido.pack(pady=20)


#? Abrir imagen con Pillow
imagen = Image.open("./folder.png")
# Redimensionar a 64x64 píxeles
imagen_redimensionada = imagen.resize((125, 125))
# Convertir a formato Tkinter
imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)

#? Mostrar en un Label con evento de clic
label = tk.Label(root, image=imagen_tk, cursor="hand2")
label.bind("<Button-1>", lambda event: abrir_nueva_ventana())  # Clic izquierdo
label.pack(pady=20)


# # Crear una etiqueta con "Hola Mundo"
fuente_personalizada = font.Font(family="Arial", size=24, weight="bold")
etiqueta = tk.Label(
    root,
    text="¡Hola Mundo!",
    font=fuente_personalizada,
    fg="#f0f0f0",  # Color del texto
    bg="#0A0A23"   # Color de fondo de la etiqueta
)

# # # Posicionar la etiqueta en el centro
etiqueta.pack(expand=True)

# # Crear un botón para cerrar
boton_cerrar = tk.Button(
    root,
    text="Cerrar",
    command=root.quit, # Acción para cerrar la ventana
    bg="#006A67",
    fg="white",
    font=("Arial", 12),
    padx=20,
    pady=10,
    cursor="hand2"
)
boton_cerrar.pack(pady=20)

# # Centrar la ventana en la pantalla
root.update_idletasks()
ancho_ventana = root.winfo_width()
alto_ventana = root.winfo_height()
x = (root.winfo_screenwidth() // 2) - (ancho_ventana // 2)
y = (root.winfo_screenheight() // 2) - (alto_ventana // 2)
root.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

# Iniciar el bucle principal
root.mainloop()