import tkinter as tk
from tkinter import messagebox
import json
from datetime import date

# File to store habit data
DATA_FILE = "habits.json"

# Load or initialize data
def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Add a new habit
def add_habit():
    habit_name = habit_entry.get().strip()
    if habit_name:
        if habit_name in habits:
            messagebox.showerror("Error", "Habit already exists!")
        else:
            habits[habit_name] = {"streak": 0, "last_completed": ""}
            save_data(habits)
            update_habit_list()
            habit_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a habit name!")

# Mark a habit as completed
def complete_habit(habit_name):
    today = str(date.today())
    if habits[habit_name]["last_completed"] != today:
        habits[habit_name]["streak"] += 1
        habits[habit_name]["last_completed"] = today
        save_data(habits)
        update_habit_list()
    else:
        messagebox.showinfo("Info", f"You already completed '{habit_name}' today!")

# Update the GUI list of habits
def update_habit_list():
    for widget in habit_frame.winfo_children():
        widget.destroy()
    for habit, data in habits.items():
        frame = tk.Frame(habit_frame, bg="#f4f4f4", pady=5, relief="solid", bd=1)
        frame.pack(fill="x", padx=5, pady=2)
        habit_label = tk.Label(
            frame, 
            text=f"{habit} (Streak: {data['streak']})", 
            font=("Arial", 14), 
            bg="#f4f4f4", 
            fg="black"
        )
        habit_label.pack(side="left", padx=5)
        complete_button = tk.Button(
            frame, 
            text="Complete", 
            command=lambda h=habit: complete_habit(h), 
            bg="#4CAF50", 
            fg="black", 
            font=("Arial", 12), 
            activebackground="#45a049"
        )
        complete_button.pack(side="right", padx=5)

# Initialize the app window
app = tk.Tk()
app.title("Habit Tracker")
app.geometry("400x500")
app.config(bg="white")

# Load habits data
habits = load_data()

# Input field to add habits
habit_entry = tk.Entry(app, font=("Arial", 14), width=25)
habit_entry.pack(pady=10)
add_button = tk.Button(
    app, 
    text="Add Habit", 
    command=add_habit, 
    bg="#007BFF", 
    fg="black", 
    font=("Arial", 12), 
)
add_button.pack(pady=5)

# Frame to display habits
habit_frame = tk.Frame(app, bg="white")
habit_frame.pack(fill="both", expand=True, pady=10)

update_habit_list()

app.mainloop()