import os
import shutil

def delete_item(listbox, current_folder, update_callback):
    try:
        selection = listbox.curselection()
        if not selection:
            listbox.insert('end', "Error: Select an item to delete")
            return
        
        selected_item = listbox.get(selection[0])
        full_path = os.path.join(current_folder, selected_item)
        
        if not os.path.exists(full_path):
            listbox.insert('end', f"Error: '{selected_item}' does not exist")
            return
        
        if os.path.isdir(full_path):
            shutil.rmtree(full_path)
            listbox.insert('end', f"Folder '{selected_item}' deleted successfully")
        else:
            os.remove(full_path)
            listbox.insert('end', f"File '{selected_item}' deleted successfully")
        
        update_callback(current_folder)
            
    except PermissionError:
        listbox.insert('end', f"Error: Permission denied to delete '{selected_item}'")
    except Exception as e:
        listbox.insert('end', f"Error deleting: {e}")