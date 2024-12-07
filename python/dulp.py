import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 1:
            messagebox.showerror("Error", "Please enter a positive number.")
            return
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))
        password_entry.config(state="normal") 
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
        password_entry.config(state="readonly")  
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")
window = tk.Tk()
window.title("Password Generator")
window.geometry("700x500")
window.configure(bg="#f0f8ff") 
length_label = tk.Label(window, text="Password Length:", font=("Helvetica", 14), fg="#333", bg="#f0f8ff")
length_label.pack(pady=20)
length_entry = tk.Entry(window, width=30, font=("Helvetica", 12), bg="#e0e0e0", fg="#333", highlightbackground="#333", highlightthickness=1)
length_entry.pack()
generate_button = tk.Button(window, text="Generate Password", command=generate_password, width=20, font=("Helvetica", 12, "bold"), bg="#4caf50", fg="white", activebackground="#388e3c", activeforeground="white")
generate_button.pack(pady=20)
password_entry = tk.Entry(window, width=50, font=("Helvetica", 12), state="readonly", justify="center", bg="#e0e0e0", fg="#333", highlightbackground="#333", highlightthickness=1)
password_entry.pack(pady=20)
length_label.pack(anchor="center")
length_entry.pack(anchor="center")
generate_button.pack(anchor="center")
password_entry.pack(anchor="center")
window.mainloop()
