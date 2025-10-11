import subprocess
from tkinter import filedialog
import os

def load_and_execute_script(text_output):
    try:
        file_path = filedialog.askopenfilename(
            title="Select script file",
            filetypes=[("Shell scripts", "*.sh"), ("Python scripts", "*.py"), ("All files", "*.*")]
        )
        
        if not file_path:
            return
        
        text_output.insert('end', f"Executing: {file_path}\n")
        text_output.insert('end', "=" * 50 + "\n")
        
        _, extension = os.path.splitext(file_path)
        
        if extension == '.py':
            command = ['python3', file_path]
        elif extension == '.sh':
            command = ['bash', file_path]
        else:
            command = [file_path]
        
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=60
        )
        
        if result.stdout:
            text_output.insert('end', result.stdout)
        if result.stderr:
            text_output.insert('end', f"Error:\n{result.stderr}")
        
        text_output.insert('end', f"\nReturn code: {result.returncode}\n")
        text_output.insert('end', "=" * 50 + "\n")
        
    except subprocess.TimeoutExpired:
        text_output.insert('end', "Error: Script timeout (60s)\n")
    except Exception as e:
        text_output.insert('end', f"Error loading script: {e}\n")
    
    text_output.see('end')

    #! En el readme indicar que esn la carpeta test estan unos script de prueba para trabajar con esta funcionalidad