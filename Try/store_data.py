import csv

# Function to create and write the CSV file
def create_csv_file():
    number_system = {'00000': 'blank', '00001': 'A', '00010': 'B', '00011': 'C', '00100': 'D',
                     '00101': 'E', '00110': 'F', '00111': 'G', '01000': 'H', '01001': 'I',
                     '01010': 'J', '01011': 'K', '01100': 'L', '01101': 'M', '01110': 'N',
                     '01111': 'O', '10000': 'P', '10001': 'Q', '10010': 'R', '10011': 'S',
                     '10100': 'T', '10101': 'U', '10110': 'V', '10111': 'W', '11000': 'X',
                     '11001': 'Y', '11010': 'Z'}

    with open('number_system.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['5_digit_number', 'character'])

        for number, char in number_system.items():
            csv_writer.writerow([number, char])

# Function to get 5-digit number system for a given character
def get_number_system(character):
    with open('number_system.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)  # Skip header row
        for row in csv_reader:
            if row[1] == character.upper():
                return row[0]
    return "Character not found in the number system"

# Uncomment the line below to create the CSV file initially
create_csv_file()

# Ask the user for a character
user_character = input("Enter a character: ")

# Get and display the 5-digit number system for the entered character
result = get_number_system(user_character)
print(f"The 5-digit number system for '{user_character}' is: {result}")
