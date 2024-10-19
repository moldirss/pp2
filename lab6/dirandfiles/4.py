def count_lines_in_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return len(lines)

# Example usage:
file_path = 'example.txt'
line_count = count_lines_in_file(file_path)
print(f"Number of lines in {file_path}: {line_count}")
