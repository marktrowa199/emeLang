import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import os 
from datetime import datetime

FILENAME = "tasks.txt"  # fixed typo

# --- File Handling ---
def load_tasks():
    if not os.path.exists(FILENAME):  # fixed typo
        return []
    with open(FILENAME, "r") as file:
        tasks = []
        for line in file.readlines():
            parts = line.strip().split(" | ")
            if len(parts) == 3:
                tasks.append({"task": parts[0], "deadline": parts[1], "status": parts[2]})
        return tasks

def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for t in tasks:
            file.write(f"{t['task']} | {t['deadline']} | {t['status']}\n")  # fixed typo

# --- GUI Functions ---

def refresh_listbox():
    listbox.delete(0, tk.END)
    for i, t in enumerate(tasks, start=1):
        listbox.insert(tk.END, f"{i}. {t['task']} ({t['deadline']}) - [{t['status']}]")  # fixed typo

def add_task():
    task_name = simpledialog.askstring("Add Task", "Enter task name: ")  # fixed typo
    if not task_name:
        return
    
    deadline = simpledialog.askstring("Add Deadline", "Enter deadline (YYYY-MM-DD): ")
    try:
        datetime.strptime(deadline, "%Y-%m-%d") #validate format
    except:
        messagebox.showerror("Error", "Invalid date format! Use YYYY-MM-DD")
        return
    tasks.append({"task": task_name, "deadline": deadline, "status": "Not Done"})
    save_tasks(tasks)
    refresh_listbox()

def mark_done():
    selection = listbox.curselection()
    if not selection:
        messagebox.showwarning("Warning", "Select a task first!")
        return
    index = selection[0]
    tasks[index]['status'] = "Done"
    save_tasks(tasks)
    refresh_listbox()
    messagebox.showinfo("Marked Done", f"Task '{tasks[index]['task']}' marked as done.")

def remove_task():
    selection = listbox.curselection()
    if not selection:
        messagebox.showwarning("Warning", "Select a task first!")
        return
    index = selection[0]
    removed = tasks.pop(index)
    save_tasks(tasks)
    refresh_listbox()
    messagebox.showinfo("Removed", f"Task '{removed['task']}' removed.")

# ---Main Window ---

root = tk.Tk()
root.title("To-Do List with Deadlines & Status")
root.geometry("500x400")

tasks = load_tasks()

listbox = tk.Listbox(root, width=60, height=15)
listbox.pack(pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack()

tk.Button(btn_frame, text="➕ Add Task", command=add_task).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="✅ Mark Done", command=mark_done).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="❌ Remove Task", command=remove_task).grid(row=0, column=2, padx=5)

refresh_listbox()
root.mainloop()