import tkinter as tk
from tkinter import scrolledtext
from src.config.styles import button_config
from src.gui.common.windows import create_secondary_window
from src.gui.shell.execute import execute_command
from src.gui.shell.load_script import load_and_execute_script

def create_shell():
    window = create_secondary_window("Shell Terminal", 800, 600)
    
    text_output = scrolledtext.ScrolledText(window, width=90, height=25, font=("Courier", 10), bg="black", fg="white")
    text_output.pack(pady=10, padx=10)
    
    frame_input = tk.Frame(window)
    frame_input.pack(pady=5)
    
    tk.Label(frame_input, text="Command:", font=("Arial", 12)).pack(side=tk.LEFT, padx=5)
    
    entry_command = tk.Entry(frame_input, width=50, font=("Courier", 11))
    entry_command.pack(side=tk.LEFT, padx=5)
    entry_command.bind('<Return>', lambda e: execute_command(entry_command, text_output))
    
    frame_buttons = tk.Frame(window)
    frame_buttons.pack(pady=10)
    
    btn_execute = tk.Button(frame_buttons, text="Execute", 
                           command=lambda: execute_command(entry_command, text_output), 
                           **button_config)
    btn_load = tk.Button(frame_buttons, text="Load Script", 
                        command=lambda: load_and_execute_script(text_output), 
                        **button_config)
    btn_clear = tk.Button(frame_buttons, text="Clear", 
                         command=lambda: text_output.delete('1.0', 'end'), 
                         **button_config)
    
    btn_execute.pack(side=tk.LEFT, padx=10)
    btn_load.pack(side=tk.LEFT, padx=10)
    btn_clear.pack(side=tk.LEFT, padx=10)
    
    text_output.insert('end', "Welcome to Shell Terminal\n")
    text_output.insert('end', "=" * 50 + "\n")