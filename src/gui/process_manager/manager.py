import tkinter as tk
from src.config.styles import button_config
from src.gui.common.windows import create_secondary_window
from src.gui.process_manager.list_processes import list_processes
from src.gui.process_manager.terminate import terminate_process

def create_process_manager():
    window = create_secondary_window("Process Manager", 800, 500)
    
    listbox = tk.Listbox(window, width=100, height=20, font=("Courier", 10))
    listbox.pack(pady=10)
    
    frame_buttons = tk.Frame(window)
    frame_buttons.pack(pady=10)
    
    btn_list = tk.Button(frame_buttons, text="List Processes", 
                         command=lambda: list_processes(listbox), 
                         **button_config)
    btn_terminate = tk.Button(frame_buttons, text="Terminate Process", 
                              command=lambda: terminate_process(listbox), 
                              **button_config)
    
    btn_list.pack(side=tk.LEFT, padx=10)
    btn_terminate.pack(side=tk.LEFT, padx=10)