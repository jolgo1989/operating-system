import os

def open_folder(listbox, current_folder, update_callback):
    try:
        selection = listbox.curselection()
        if not selection:
            listbox.insert('end', "Error: Select a folder first")
            return current_folder
        
        selected_folder = listbox.get(selection[0])
        full_path = os.path.join(current_folder, selected_folder)
        
        if not os.path.isdir(full_path):
            listbox.insert('end', f"Error: '{selected_folder}' is not a folder")
            return current_folder
        
        update_callback(full_path)
        return full_path
            
    except Exception as e:
        listbox.insert('end', f"Error navigating: {e}")
        return current_folder

def go_back(current_folder, update_callback, listbox):
    try:
        parent_folder = os.path.dirname(current_folder)
        
        if parent_folder != current_folder:
            update_callback(parent_folder)
            return parent_folder
        else:
            listbox.insert('end', "Already at root folder")
            return current_folder
            
    except Exception as e:
        listbox.insert('end', f"Error going back: {e}")
        return current_folder