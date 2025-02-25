import tkinter as tk
from datetime import datetime

# Function to calculate age
def calculate_age():
    try:
        birth_date = datetime.strptime(entry.get(), "%Y-%m-%d")
        today = datetime.today()

        # Calculate years, months, and days
        years = today.year - birth_date.year
        months = today.month - birth_date.month
        days = today.day - birth_date.day

        # Adjust for negative months or days
        if days < 0:
            months -= 1
            days += 31  # Approximate days in a month
        if months < 0:
            years -= 1
            months += 12

        result_label.config(text=f"Your age is: {years} years, {months} months, and {days} days", fg="green")
    except ValueError:
        result_label.config(text="Invalid date format! Use YYYY-MM-DD", fg="red")

# Create the main window
root = tk.Tk()
root.title("Age Calculator")
root.geometry("400x250")
root.configure(bg="#f0f0f0")

# Add a label for instructions
instruction_label = tk.Label(root, text="Enter your birth date (YYYY-MM-DD):", font=("Arial", 12), bg="#f0f0f0")
instruction_label.pack(pady=10)

# Add an entry field for the birth date
entry = tk.Entry(root, font=("Arial", 12), width=20)
entry.pack(pady=10)

# Add a button to calculate age
calculate_button = tk.Button(root, text="Calculate Age", font=("Arial", 12), command=calculate_age, bg="#4CAF50", fg="white")
calculate_button.pack(pady=10)

# Add a label to display the result
result_label = tk.Label(root, text="", font=("Arial", 12), bg="#f0f0f0")
result_label.pack(pady=10)

# Add a reset button to clear the input and result
def reset():
    entry.delete(0, tk.END)
    result_label.config(text="")

reset_button = tk.Button(root, text="Reset", font=("Arial", 12), command=reset, bg="#FF5733", fg="white")
reset_button.pack(pady=10)

# Run the application
root.mainloop()