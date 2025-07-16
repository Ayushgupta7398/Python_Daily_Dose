import tkinter as tk

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    try:
        selected = task_listbox.curselection()
        task_listbox.delete(selected)
    except:
        pass

def save_tasks():
    with open("tasks.txt", "w") as f:
        tasks = task_listbox.get(0, tk.END)
        for task in tasks:
            f.write(task + "\n")

def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            for line in f:
                task_listbox.insert(tk.END, line.strip())
    except FileNotFoundError:
        pass

root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x500")

tk.Label(root, text="📝 My To-Do List", font=("Arial", 18)).pack(pady=10)

task_entry = tk.Entry(root, font=("Arial", 14))
task_entry.pack(pady=10)

tk.Button(root, text="Add Task", command=add_task).pack()

task_listbox = tk.Listbox(root, width=40, height=10, font=("Arial", 12))
task_listbox.pack(pady=10)

tk.Button(root, text="Delete Selected", command=delete_task).pack(pady=5)
tk.Button(root, text="Save Tasks", command=save_tasks).pack(pady=5)
tk.Button(root, text="Load Tasks", command=load_tasks).pack(pady=5)

load_tasks()
root.mainloop()


