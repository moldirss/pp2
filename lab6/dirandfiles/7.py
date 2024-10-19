import shutil

def copy_file(source_path, destination_path):
    shutil.copyfile(source_path, destination_path)
    print(f"Copied from {source_path} to {destination_path}")

# Example usage:
source_file = 'source.txt'
destination_file = 'destination.txt'
copy_file(source_file, destination_file)
