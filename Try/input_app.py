import tkinter as tk

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

        # Further code using the user input can be added here

if __name__ == "__main__":
    root = tk.Tk()
    app = InputApp(root)
    root.mainloop()
