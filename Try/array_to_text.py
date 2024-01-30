import csv

def read_csv(file_path):
    number_mapping = {}
    with open(file_path, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)  # Skip the header row
        for row in csv_reader:
            binary_digits = row[0]
            character = row[1] if row[1] else ' '
            number_mapping[binary_digits] = character
    return number_mapping

def find_character(input_list, number_mapping):
    binary_str = ''.join(map(str, input_list))
    return number_mapping.get(binary_str, 'Not found')

# CSV file path
csv_file_path = 'number_system.csv'

# Read the CSV file
number_mapping = read_csv(csv_file_path)

# Example input
input_list = [1, 1, 0, 0, 0]

# Find the associated character
result = find_character(input_list, number_mapping)

# Display the result
print(f"Input: {input_list}")
print(f"Associated Character: {result}")
