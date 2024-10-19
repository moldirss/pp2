import os

def test_path(path):
    if os.path.exists(path):
        dir_name = os.path.dirname(path)
        file_name = os.path.basename(path)
        print(f"Path exists.")
        print(f"Directory: {dir_name}")
        print(f"File: {file_name}")
    else:
        print(f"Path does not exist.")

# Example usage:
path = '/path/to/test'
test_path(path)
