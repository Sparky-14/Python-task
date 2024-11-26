# <--------TASK 1 ------->
# <----RENAME---->

import os

def rename_files_in_folder(folder_path):

    if not os.path.exists(folder_path):
        print("Error: The folder '{}' does not exist.".format(folder_path))
        return

  
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    
    if not files:
        print("The folder is empty. No files to rename.")
        return

    
    files.sort()

    print("Renaming files...")
    for idx, file_name in enumerate(files, start=1):
        
        file_path = os.path.join(folder_path, file_name)
        file_extension = os.path.splitext(file_name)[1]

        
        new_file_name = "{}{}".format(idx, file_extension)
        new_file_path = os.path.join(folder_path, new_file_name)

        
        try:
            os.rename(file_path, new_file_path)
            print("File '{}' renamed to '{}'".format(file_name, new_file_name))
        except PermissionError:
            print("Error: Unable to rename file '{}' due to permission issues.".format(file_name))
        except Exception as e:
            print("Error: Unable to rename file '{}' due to {}.".format(file_name, str(e)))

    print("Renaming completed.")

if __name__ == "__main__":
    
    folder_path = input("Please enter the path to the folder: ").strip()
    rename_files_in_folder(folder_path)
