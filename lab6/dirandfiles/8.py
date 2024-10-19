import os

def delete_file(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)
            print(f"File deleted: {path}")
        else:
            print(f"Access denied: Cannot delete {path}")
    else:
        print(f"File does not exist: {path}")

# Example usage:
file_path = 'file_to_delete.txt'
delete_file(file_path)
