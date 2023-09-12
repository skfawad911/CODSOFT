import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    try:
        selected_task_index = task_list.curselection()[0]
        task_list.delete(selected_task_index)
    except IndexError:
        pass

def update_task():
    try:
        selected_task_index = task_list.curselection()[0]
        new_task = task_entry.get()
        if new_task:
            task_list.delete(selected_task_index)
            task_list.insert(selected_task_index, new_task)
            task_entry.delete(0, tk.END)
    except IndexError:
        pass

app = tk.Tk()
app.title("To-Do List")
app.geometry("400x650+400+100")


image = Image.open("image/todo-header.png")
image = image.resize((500, 100))
photo = ImageTk.PhotoImage(image)

image_label = tk.Label(app, image=photo)
image_label.pack(padx=20, pady=10)

image_label.image = photo


frame = tk.Frame(app)
frame.pack(pady=10)

task_entry = tk.Entry(frame, font=("Arial", 12), bd=2, relief=tk.GROOVE)
task_entry.pack(fill=tk.BOTH, expand=True, padx=20, side=tk.LEFT)

add_button = tk.Button(frame, text="Add", font=("Arial", 12), bg="green", fg="white", command=add_task)
add_button.pack(pady=5, side=tk.LEFT)

remove_button = tk.Button(frame, text="Remove", font=("Arial", 12), bg="red", fg="white", command=remove_task)
remove_button.pack(pady=5, side=tk.LEFT)

update_button = tk.Button(frame, text="Update", font=("Arial", 12), bg="blue", fg="white", command=update_task)
update_button.pack(pady=5, side=tk.LEFT)

task_list = tk.Listbox(app, selectbackground="blue", selectmode=tk.SINGLE, font=("Arial", 12), bd=2, relief=tk.GROOVE, bg="lightgray")
task_list.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

app.mainloop()
