import os

def list_directories_files(path):
    directories = []
    files = []
    all_items = os.listdir(path)
    
    for item in all_items:
        if os.path.isdir(os.path.join(path, item)):
            directories.append(item)
        elif os.path.isfile(os.path.join(path, item)):
            files.append(item)

    return directories, files, all_items

# Example usage:
path = '.'  # specify your path here
dirs, files, all_items = list_directories_files(path)
print(f"Directories: {dirs}")
print(f"Files: {files}")
print(f"All Items: {all_items}")
