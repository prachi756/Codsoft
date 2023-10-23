import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to delete.")

def edit_task():
    try:
        selected_task_index = listbox.curselection()[0]
        selected_task = listbox.get(selected_task_index)
        entry.delete(0, tk.END)
        entry.insert(tk.END, selected_task)
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to edit.")
screen = tk.Tk()
screen.title("To-Do List")
entry = tk.Entry(screen, width=30)
entry.pack(pady=10)
listbox = tk.Listbox(screen, width=30)
listbox.pack()
add_button = tk.Button(screen, text="Add Task", command=add_task)
edit_button = tk.Button(screen, text="Edit Task", command=edit_task)
delete_button = tk.Button(screen, text="Delete Task", command=delete_task)
add_button.pack()
edit_button.pack()
delete_button.pack()
screen.mainloop()