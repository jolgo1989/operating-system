import tkinter as tk
from src.config.styles import button_config
from src.gui.file_explorer import create_file_explorer
from src.gui.process_manager import create_process_manager

def launch_main_menu():
    root = tk.Tk()
    root.title("Educational Operating System")
    root.geometry("400x400")
    root.configure(bg="#f0f0f0")

    tk.Label(root, text="Main Menu", font=("Arial", 16), bg="#f0f0f0").pack(pady=20)

    tk.Button(root, text="📂 File Explorer", command=create_file_explorer, **button_config).pack(pady=10)
    tk.Button(root, text="⚙️ Process Manager", command=create_process_manager, **button_config).pack(pady=10)

    root.mainloop()

