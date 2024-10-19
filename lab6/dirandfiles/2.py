import os

def check_access(path):
    if os.path.exists(path):
        print(f"Path exists: {path}")
        print(f"Readable: {os.access(path, os.R_OK)}")
        print(f"Writable: {os.access(path, os.W_OK)}")
        print(f"Executable: {os.access(path, os.X_OK)}")
    else:
        print(f"Path does not exist: {path}")

# Example usage:
path = '/path/to/check'
check_access(path)
