# Exploring Python's OS Module

import os

def list_directory_contents(path):
    # List and print all files and subdirectories in the given path
    print(path)

    try:
        file_list = os.listdir(path)
    except OSError:
        return
    
    for i in file_list:
        full_path_display = os.path.join(path, i)
        print(full_path_display)


    
list_directory_contents() #Used my Code Temple directory to test out the code.