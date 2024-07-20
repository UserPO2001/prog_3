import tkinter as tk

class StudentGreetingApp:
    def __init__(self, root):
        # Titel van het scherm
        root.title("Student Begroeting Applicatie")
        # kleur van het ventster
        root.configure(bg="#f6b4cd")


        # Label met aangepaste voorgrond- en achtergrondkleur en welkomsttekst
        self.welcome_label = tk.Label(root, text="Welkom Student!", bg="#3498db", fg="#ffffff", font=("Arial", 14))
        self.welcome_label.pack(pady=10)

        # Invoerveld met aangepaste kleuren en lettertype
        self.name_entry = tk.Entry(root, bg="#ecf0f1", fg="#2c3e50", font=("Arial", 12))
        self.name_entry.pack(pady=10)

        # Knop om begroeting te activeren
        self.greet_button = tk.Button(root, text="Begroet", command=self.greet_student, bg="#27ae60", fg="#ffffff", font=("Arial", 12))
        self.greet_button.pack(pady=10)

    def greet_student(self):
        # Haal de ingevoerde naam op
        student_name = self.name_entry.get()

        # Toon een begroetingsbericht in de console (je kunt dit aanpassen zoals gewenst)
        print(f"Hallo {student_name}! Welkom bij de applicatie.")

if __name__ == "__main__":
    # Maak een Tkinter-venster
    root = tk.Tk()

    # Maak een object van de StudentGreetingApp-klasse
    app = StudentGreetingApp(root)

    # Start de Tkinter main loop
    root.mainloop()
