def write_list_to_file(file_path, data_list):
    with open(file_path, 'w') as file:
        for item in data_list:
            file.write(f"{item}\n")

# Example usage:
data_list = ['apple', 'banana', 'cherry']
write_list_to_file('fruits.txt', data_list)
