import tkinter as tk

def create_secondary_window(title="Window", width=600, height=400):
    window = tk.Toplevel()
    window.title(title)
    window.geometry(f"{width}x{height}")
    return window