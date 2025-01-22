import tkinter as tk
from tkinter import messagebox

users = {
    "amin": "12345",
    "ali": "54321",
    "zahra": "55132"
}


def login():
    username = username_entry.get()
    password = password_entry.get()

    if username in users and users[username] == password:
        messagebox.showinfo("Login Success", "Welcome!")
        root.destroy()  
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")
           
root = tk.Tk()
root.title("Login Page")
root.geometry("300x200")
root.resizable(False, False)


tk.Label(root, text="Login", font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Username:", font=("Arial", 12)).pack(anchor="w", padx=20)
username_entry = tk.Entry(root, font=("Arial", 12))
username_entry.pack(fill="x", padx=20, pady=5)

tk.Label(root, text="Password:", font=("Arial", 12)).pack(anchor="w", padx=20)
password_entry = tk.Entry(root, font=("Arial", 12), show="*")
password_entry.pack(fill="x", padx=20, pady=5)

login_button = tk.Button(root, text="Login", font=("Arial", 12), command=login)
login_button.pack(pady=10)


root.mainloop()
