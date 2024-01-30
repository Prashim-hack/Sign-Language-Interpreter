import tkinter as tk
import csv
from cvzone.SerialModule import SerialObject
import time

def char_to_binary(char):
    binary_str = format(ord(char) - ord('A') + 1, '05b')
    return binary_str

def get_number_system(user_char):
    user_char = user_char.upper()

    if user_char.isalpha() and len(user_char) == 1:
        binary_representation = char_to_binary(user_char)
        binary_array = list(binary_representation)
        return binary_array

    else:
        print("Invalid input. Please enter a single alphabetical character.")


def separate_characters(word):
    separated_characters = list(word)
    return separated_characters

def_arr = [0,0,0,0,0]
mySerial = SerialObject("COM3",9600,1)

class InputApp:
    def __init__(self, root):
        self.root = root
        self.root.title("String Input App")

        # Variable to store user input
        self.user_input_var = tk.StringVar()

        # Label and Entry for user input
        label = tk.Label(root, text="Enter a string:")
        label.pack(pady=10)

        entry = tk.Entry(root, textvariable=self.user_input_var)
        entry.pack(pady=10)

        # Button to submit user input
        submit_button = tk.Button(root, text="Submit", command=self.submit_input)
        submit_button.pack(pady=10)



    def submit_input(self):
        user_input = self.user_input_var.get()
        print(f"User input: {user_input}")
        result_label = tk.Label(root, textvariable=user_input)
        result_label.pack(pady=10)

        user_input = user_input.upper()
        result = separate_characters(user_input)
        
        for element in result:
            printing_arr = get_number_system(element)
            mySerial.sendData(printing_arr)
            print(f"Showing {element} with finger {printing_arr}")
            time.sleep(2) 
        mySerial.sendData(def_arr)       


if __name__ == "__main__":
    root = tk.Tk()
    app = InputApp(root)
    root.mainloop()
