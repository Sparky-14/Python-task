# <----TASK 2 ----->
# <-----Zipping a Folder----->

import os
import zipfile
import sys

def zip_folder(folder_path, output_zip_path=None):
  
    try:
        
        if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
            print("Error: '{}' is not a valid folder path.".format(folder_path))
            return
        
        
        folder_name = os.path.basename(os.path.normpath(folder_path))
        if not output_zip_path:
            output_zip_path = os.path.join(os.path.dirname(folder_path), "{}.zip".format(folder_name))
        
        
        with zipfile.ZipFile(output_zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, folder_path)  
                    zipf.write(file_path, arcname)
                
                for dir in dirs:
                    dir_path = os.path.join(root, dir)
                    if not os.listdir(dir_path):  
                        arcname = os.path.relpath(dir_path, folder_path) + "/"
                        zipf.writestr(arcname, "")  

        print("Success: Folder '{}' has been zipped to '{}'.".format(folder_path, output_zip_path))

    except PermissionError:
        print("Error: Permission denied. Ensure you have the right permissions.")
    except Exception as e:
        print("An unexpected error occurred: {}".format(e))

if __name__ == "__main__":
    
    folder_path = raw_input("Enter the path to the folder you want to zip: ").strip()  
    if not folder_path:
        print("Error: No folder path provided.")
        sys.exit(1)
    
   
    custom_name = raw_input("Enter a custom name for the .zip file (or press Enter to use the default name): ").strip()
    output_zip_path = None if not custom_name else os.path.join(os.path.dirname(folder_path), "{}.zip".format(custom_name))
    
  
    zip_folder(folder_path, output_zip_path)

