import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Define the Student class
class Student:
    def __init__(self, birthdate):
        self.birthdate = datetime.strptime(birthdate, "%Y-%m-%d")

    def calculate_age(self):
        today = datetime.today()
        age = today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
        return age

# Define the AgeCalculatorApp class
class AgeCalculatorApp:
    def __init__(self, root):
        self.root = root
        root.title("Age Calculator")

        # Labels and Entry widgets
        self.birthdate_label = tk.Label(root, text="Enter your birthdate (YYYY-MM-DD):")
        self.birthdate_label.grid(row=0, column=0, padx=10, pady=10)

        self.birthdate_entry = tk.Entry(root)
        self.birthdate_entry.grid(row=0, column=1, padx=10, pady=10)

        # Buttons
        self.submit_button = tk.Button(root, text="Submit", command=self.calculate_age)
        self.submit_button.grid(row=1, column=0, padx=10, pady=10)

        self.clear_button = tk.Button(root, text="Clear", command=self.clear_input)
        self.clear_button.grid(row=1, column=1, padx=10, pady=10)

        # Result Label
        self.result_label = tk.Label(root, text="")
        self.result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def calculate_age(self):
        birthdate = self.birthdate_entry.get()
        try:
            student = Student(birthdate)
            age = student.calculate_age()
            if age > 115:
                messagebox.showerror("Invalid Age", "Age cannot be greater than 115 years.")
            else:
                self.result_label.config(text=f"You are {age} years old.")
        except ValueError:
            messagebox.showerror("Invalid Date", "Please enter a valid date in the format YYYY-MM-DD")

    def clear_input(self):
        self.birthdate_entry.delete(0, tk.END)
        self.result_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = AgeCalculatorApp(root)
    root.mainloop()
