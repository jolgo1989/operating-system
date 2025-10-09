import psutil #Biblioteca multiplataforma para monitorización de procesos y sistemas.

def terminate_process(listbox):
    try:
        selection = listbox.curselection()
        if not selection:
            listbox.insert('end', "Error: Select a process to terminate")
            return
        
        selected_text = listbox.get(selection[0])
        pid = int(selected_text.split("PID: ")[1].split(" |")[0])
        
        process = psutil.Process(pid)
        process.terminate()
        listbox.insert('end', f"Process {pid} terminated successfully")
        
    except psutil.NoSuchProcess:
        listbox.insert('end', f"Error: Process {pid} not found")
    except psutil.AccessDenied:
        listbox.insert('end', f"Error: Permission denied to terminate process {pid}")
    except Exception as e:
        listbox.insert('end', f"Error terminating process: {e}")