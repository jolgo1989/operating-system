import subprocess

def execute_command(entry, text_output):
    command = entry.get()
    if not command.strip():
        text_output.insert('end', "Error: Enter a command\n")
        return
    
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=30
        )
        
        text_output.insert('end', f"$ {command}\n")
        
        if result.stdout:
            text_output.insert('end', result.stdout)
        if result.stderr:
            text_output.insert('end', f"Error:\n{result.stderr}")
        
        text_output.insert('end', f"\nReturn code: {result.returncode}\n")
        text_output.insert('end', "-" * 50 + "\n")
        
        entry.delete(0, 'end')
        
    except subprocess.TimeoutExpired:
        text_output.insert('end', "Error: Command timeout (30s)\n")
    except Exception as e:
        text_output.insert('end', f"Error executing: {e}\n")
    
    text_output.see('end')

    #! En el readme que estos comandos se pueden utilizar como comandos de prueba en la terminal
    # ls -la
    # pwd
    # echo "Hello from shell"
    # whoami
    # date