import tkinter as tk
from tkinter import messagebox
import json

# Define the file to store tasks
FILENAME = "tasks.json"

# Function to load tasks from a file
def load_tasks():
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to save tasks to a file
def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        json.dump(tasks, file)

# Main application class
class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        
        self.tasks = load_tasks()
        
        # Create GUI components
        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.pack(pady=10)
        
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)
        
        self.tasks_listbox = tk.Listbox(root, width=50, height=10)
        self.tasks_listbox.pack(pady=10)
        
        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack(pady=5)
        
        self.load_tasks()
    
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.tasks_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
            save_tasks(self.tasks)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")
    
    def load_tasks(self):
        for task in self.tasks:
            self.tasks_listbox.insert(tk.END, task)
    
    def remove_task(self):
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            task = self.tasks_listbox.get(selected_task_index)
            self.tasks_listbox.delete(selected_task_index)
            self.tasks.remove(task)
            save_tasks(self.tasks)
        else:
            messagebox.showwarning("Warning", "You must select a task to remove.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
