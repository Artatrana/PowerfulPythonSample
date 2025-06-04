import tkinter as tk
from tkinter import messagebox
import os
import json

# File to store user credentials
USER_FILE = "users.json"

# Create users.json if it doesn't exist
if not os.path.exists(USER_FILE):
    with open(USER_FILE, "w") as file:
        json.dump({"admin": "pass123"}, file)

def load_users():
    with open(USER_FILE, "r") as file:
        return json.load(file)

def save_users(users):
    with open(USER_FILE, "w") as file:
        json.dump(users, file)

def show_dashboard(username):
    dashboard = tk.Toplevel()
    dashboard.title("Dashboard")
    tk.Label(dashboard, text=f"Welcome, {username}!", font=("Arial", 16)).pack(pady=20)
    tk.Button(dashboard, text="Logout", command=lambda: [dashboard.destroy(), root.deiconify()]).pack(pady=10)

def login(event=None):  # allow calling with or without event
    username = username_entry.get()
    password = password_entry.get()
    users = load_users()
    if username in users and users[username] == password:
        root.withdraw()  # Hide login window
        show_dashboard(username)
    else:
        messagebox.showerror("Login", "Invalid username or password.")

def register():
    username = username_entry.get()
    password = password_entry.get()
    users = load_users()
    if username in users:
        messagebox.showerror("Register", "Username already exists.")
    else:
        users[username] = password
        save_users(users)
        messagebox.showinfo("Register", "Registration successful!")

# GUI Setup
root = tk.Tk()
root.title("Login System")

tk.Label(root, text="Username:").pack()
username_entry = tk.Entry(root)
username_entry.pack()

tk.Label(root, text="Password:").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()
password_entry.bind("<Return>", login)  # Pressing Enter triggers login

tk.Button(root, text="Login", command=login).pack(pady=5)
tk.Button(root, text="Register", command=register).pack()

root.mainloop()