import psutil #Biblioteca multiplataforma para monitorización de procesos y sistemas.

def list_processes(listbox):
    listbox.delete(0, 'end')
    try:
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
            try:
                info = proc.info
                processes.append(f"PID: {info['pid']} | {info['name']} | CPU: {info['cpu_percent']:.1f}% | MEM: {info['memory_percent']:.1f}%")
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
        
        if processes:
            for process in processes:
                listbox.insert('end', process)
        else:
            listbox.insert('end', "No processes found.")
    except Exception as e:
        listbox.insert('end', f"Error: {e}")
#* Observación:
# Utilizar este comando en la terminal para crear procesos de prueba:
#   sleep 300 &
#   echo $!
#
# Ejemplo de salida: 12345
# La próxima vez que ejecutes el comando, el PID será diferente.
# Ejemplo de salida: 12346
#
# Se debe buscar el PID del proceso que se desea eliminar.
# Cuando se elimine el proceso, en la terminal aparecerá el mensaje:
#   [1]+ Terminated sleep 300
#
# Cada vez que se ejecuta el comando "sleep 300 &", se inicia un proceso
# en segundo plano que duerme durante 300 segundos (5 minutos). El símbolo
# "&" al final del comando indica que el proceso debe ejecutarse en segundo
# plano, permitiendo seguir utilizando la terminal para otros comandos.