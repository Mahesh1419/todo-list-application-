import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.tasks = tk.Listbox(root, selectmode=tk.SINGLE, width=40, height=10)
        self.tasks.pack(pady=10)

        self.entry = tk.Entry(root, width=30)
        self.entry.pack(pady=5)

        # Buttons
        tk.Button(root, text="Add Task", command=self.add_task).pack(pady=5)
        tk.Button(root, text="Update Task", command=self.update_task).pack(pady=5)
        tk.Button(root, text="Mark as Completed", command=self.mark_completed).pack(pady=5)
        tk.Button(root, text="Remove Task", command=self.remove_task).pack(pady=5)

    def add_task(self):
        task = self.entry.get()
        if task:
            self.tasks.insert(tk.END, task)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def update_task(self):
        selected_task_index = self.tasks.curselection()
        if selected_task_index:
            new_task = self.entry.get()
            if new_task:
                self.tasks.delete(selected_task_index)
                self.tasks.insert(selected_task_index, new_task)
                self.entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "Please enter a new task.")
        else:
            messagebox.showwarning("Warning", "Please select a task to update.")

    def mark_completed(self):
        selected_task_index = self.tasks.curselection()
        if selected_task_index:
            task = self.tasks.get(selected_task_index)
            if not task.startswith("[Completed] "):
                self.tasks.delete(selected_task_index)
                self.tasks.insert(tk.END, "[Completed] " + task)
            else:
                messagebox.showwarning("Warning", "Task is already marked as completed.")
        else:
            messagebox.showwarning("Warning", "Please select a task to mark as completed.")

    def remove_task(self):
        selected_task_index = self.tasks.curselection()
        if selected_task_index:
            self.tasks.delete(selected_task_index)
        else:
            messagebox.showwarning("Warning", "Please select a task to remove.")


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()
