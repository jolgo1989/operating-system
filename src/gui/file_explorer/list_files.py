import os

def list_files(listbox, folder):
    listbox.delete(0, 'end')
    try:
        files = os.listdir(folder)
        if files:
            for file in files:
                listbox.insert('end', file)
        else:
            listbox.insert('end', "Folder is empty.")
    except Exception as e:
        listbox.insert('end', f"Error: {e}")
