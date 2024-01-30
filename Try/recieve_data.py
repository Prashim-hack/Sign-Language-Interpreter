import csv
def char_to_binary(char):
    binary_str = format(ord(char) - ord('A') + 1, '05b')
    return binary_str

def get_number_system(user_char):
    user_char = user_char.upper()

    if user_char.isalpha() and len(user_char) == 1:
        binary_representation = char_to_binary(user_char)
        binary_array = list(binary_representation)
        return binary_array
        print(f"Binary representation of {user_char}: {binary_representation}")
        print(f"Binary array: {binary_array}")
    else:
        print("Invalid input. Please enter a single alphabetical character.")


def separate_characters(word):
    separated_characters = list(word)
    return separated_characters


user_input = input("Enter a word: ")

result = separate_characters(user_input)


for element in result:
    printing_arr = get_number_system(element)
    print(f"Binary representation of {element} is {printing_arr}")

