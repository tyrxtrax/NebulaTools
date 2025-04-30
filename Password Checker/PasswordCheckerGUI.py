import re
import tkinter as tk
from tkinter import messagebox

def check_password_strength(password):
    strength = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for uppercase letters
    if any(char.isupper() for char in password):
        strength += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")

    # Check for lowercase letters
    if any(char.islower() for char in password):
        strength += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")

    # Check for digits
    if any(char.isdigit() for char in password):
        strength += 1
    else:
        feedback.append("Password should include at least one digit.")

    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Password should include at least one special character (!@#$%^&*(), etc.).")

    # Determine strength level
    if strength == 5:
        return "Strong password!", feedback
    elif 3 <= strength < 5:
        return "Moderate password.", feedback
    else:
        return "Weak password.", feedback

def evaluate_password():
    password = password_entry.get()
    result, suggestions = check_password_strength(password)
    result_label.config(text=result, fg="green" if result == "Strong password!" else "orange" if result == "Moderate password." else "red")
    suggestions_text.delete(1.0, tk.END)
    if suggestions:
        suggestions_text.insert(tk.END, "Suggestions to improve your password:\n")
        for suggestion in suggestions:
            suggestions_text.insert(tk.END, f"- {suggestion}\n")

def toggle_password_visibility():
    if password_entry.cget("show") == "*":
        password_entry.config(show="")
        show_password_button.config(text="Hide Password")
    else:
        password_entry.config(show="*")
        show_password_button.config(text="Show Password")

# Create the main window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("300x300")
root.configure(bg="#f0f0f0")

# Title label
title_label = tk.Label(root, text="Password Strength Checker", font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#333")
title_label.pack(pady=10)

# Password entry
password_label = tk.Label(root, text="Enter your password:", font=("Arial", 12), bg="#f0f0f0", fg="#333")
password_label.pack(pady=5)
password_entry = tk.Entry(root, show="*", font=("Arial", 12), width=30)
password_entry.pack(pady=5)

# Show Password button
show_password_button = tk.Button(root, text="Show Password", font=("Arial", 10), bg="#4CAF50", fg="white", command=toggle_password_visibility)
show_password_button.pack(pady=5)

# Check button
check_button = tk.Button(root, text="Check Strength", font=("Arial", 12), bg="#4CAF50", fg="white", command=evaluate_password)
check_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"), bg="#f0f0f0")
result_label.pack(pady=5)

# Suggestions text box
suggestions_text = tk.Text(root, font=("Arial", 10), height=8, width=45, bg="#f9f9f9", wrap="word", state="normal")
suggestions_text.pack(pady=10)

# Run the application
root.mainloop()