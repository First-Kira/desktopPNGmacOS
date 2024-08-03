import os
import shutil

# Path to the desktop on macOS
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')

# Define the folder names and their corresponding file extensions
folders = {
    "PNG_Files": ['.png'],
    # Add more folders and file extensions here
}

def organize_files():
    for folder_name, extensions in folders.items():
        folder_path = os.path.join(desktop_path, folder_name)
        
        # Create the folder if it doesn't exist
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        
        # Loop through files on the desktop
        for item in os.listdir(desktop_path):
            item_path = os.path.join(desktop_path, item)
            
            # Check if the item is a file and has one of the specified extensions
            if os.path.isfile(item_path) and any(item.lower().endswith(ext) for ext in extensions):
                # Move the file to the corresponding folder
                shutil.move(item_path, folder_path)
                print(f"Moved {item} to {folder_path}")

if __name__ == "__main__":
    organize_files()

