import os
from tkinter import simpledialog, messagebox

def create_item(listbox, current_folder, update_callback):
    try:
        item_type = messagebox.askquestion("Create", "Create a folder?\n(No = Create file)")
        
        if item_type == 'yes':
            folder_name = simpledialog.askstring("Create Folder", "Enter folder name:")
            if folder_name:
                full_path = os.path.join(current_folder, folder_name)
                os.makedirs(full_path, exist_ok=True)
                listbox.insert('end', f"Folder '{folder_name}' created successfully")
                update_callback(current_folder)
        else:
            file_name = simpledialog.askstring("Create File", "Enter file name:")
            if file_name:
                full_path = os.path.join(current_folder, file_name)
                with open(full_path, 'w') as f:
                    pass
                listbox.insert('end', f"File '{file_name}' created successfully")
                update_callback(current_folder)
            
    except PermissionError:
        listbox.insert('end', "Error: Permission denied")
    except Exception as e:
        listbox.insert('end', f"Error creating: {e}")