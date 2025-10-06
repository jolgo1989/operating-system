import tkinter as tk
from src.config.settings import FOLDER
from src.config.styles import button_config
from src.gui.common.windows import create_secondary_window
from src.gui.file_explorer.list_files import list_files
from src.gui.file_explorer.open import open_folder, go_back
from src.gui.file_explorer.delete import delete_item
from src.gui.file_explorer.create import create_item

def create_file_explorer():
    current_folder = FOLDER
    window = create_secondary_window(f"File List - {current_folder}", 1100, 400)
    
    listbox = tk.Listbox(window, width=50, height=15)
    listbox.pack(pady=10)
    
    def update_folder(new_folder):
        nonlocal current_folder
        current_folder = new_folder
        window.title(f"File List - {current_folder}")
        list_files(listbox, current_folder)
    
    frame_buttons = tk.Frame(window)
    frame_buttons.pack(pady=10)
    
    btn_back = tk.Button(frame_buttons, text="← Back", 
                         command=lambda: go_back(current_folder, update_folder, listbox), 
                         **button_config)
    btn_list = tk.Button(frame_buttons, text="List Files", 
                         command=lambda: list_files(listbox, current_folder), 
                         **button_config)
    btn_change = tk.Button(frame_buttons, text="Change Folder", **button_config)
    btn_create = tk.Button(frame_buttons, text="Create", 
                          command=lambda: create_item(listbox, current_folder, update_folder), 
                          **button_config)
    btn_delete = tk.Button(frame_buttons, text="Delete", 
                          command=lambda: delete_item(listbox, current_folder, update_folder), 
                          **button_config)
    btn_open = tk.Button(frame_buttons, text="Open Folder", 
                        command=lambda: open_folder(listbox, current_folder, update_folder), 
                        **button_config)
    
    btn_back.grid(row=0, column=0, padx=5, pady=5)
    btn_list.grid(row=0, column=1, padx=10, pady=5)
    btn_open.grid(row=0, column=2, padx=5, pady=5)
    btn_create.grid(row=1, column=0, padx=5, pady=5)
    btn_change.grid(row=1, column=1, padx=15, pady=5)
    btn_delete.grid(row=1, column=2, padx=20, pady=5)