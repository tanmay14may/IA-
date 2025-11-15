import tkinter as tk
from tkinter import filedialog, messagebox

root = tk.Tk()
root.title("Simple To-Do List")
root.geometry("420x420")
tasks = []

frame = tk.Frame(root)
frame.pack(pady=10)

entry = tk.Entry(frame, width=28, font=("Arial", 14))
entry.grid(row=0, column=0, padx=6)

def refresh():
    listbox.delete(0, tk.END)
    for t in tasks:
        prefix = "✓ " if t["done"] else "  "
        listbox.insert(tk.END, prefix + t["text"])

def add_task():
    txt = entry.get().strip()
    if txt:
        tasks.append({"text": txt, "done": False})
        entry.delete(0, tk.END)
        refresh()

def toggle_done(event=None):
    sel = listbox.curselection()
    if not sel:
        return
    i = sel[0]
    tasks[i]["done"] = not tasks[i]["done"]
    refresh()
    listbox.select_set(i)

def delete_task():
    sel = listbox.curselection()
    if not sel:
        return
    del tasks[sel[0]]
    refresh()

def clear_all():
    if messagebox.askyesno("Confirm", "Clear all tasks?"):
        tasks.clear()
        refresh()

def save_tasks():
    path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files","*.txt"),("All files","*.*")])
    if not path:
        return
    with open(path, "w", encoding="utf-8") as f:
        for t in tasks:
            line = ("1" if t["done"] else "0") + "|" + t["text"] + "\n"
            f.write(line)

def load_tasks():
    path = filedialog.askopenfilename(filetypes=[("Text files","*.txt"),("All files","*.*")])
    if not path:
        return
    try:
        with open(path, "r", encoding="utf-8") as f:
            loaded = []
            for line in f:
                line = line.rstrip("\n")
                if "|" in line:
                    s, txt = line.split("|", 1)
                    loaded.append({"text": txt, "done": s == "1"})
        tasks.clear()
        tasks.extend(loaded)
        refresh()
    except Exception as e:
        messagebox.showerror("Error", str(e))

add_btn = tk.Button(frame, text="Add", width=8, command=add_task)
add_btn.grid(row=0, column=1)

listbox = tk.Listbox(root, width=48, height=14, font=("Arial", 12), activestyle="none")
listbox.pack(padx=10, pady=6)
listbox.bind("<Double-Button-1>", toggle_done)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=6)

done_btn = tk.Button(btn_frame, text="Toggle Done", width=12, command=toggle_done)
done_btn.grid(row=0, column=0, padx=4)

del_btn = tk.Button(btn_frame, text="Delete", width=10, command=delete_task)
del_btn.grid(row=0, column=1, padx=4)

clear_btn = tk.Button(btn_frame, text="Clear All", width=10, command=clear_all)
clear_btn.grid(row=0, column=2, padx=4)

save_btn = tk.Button(btn_frame, text="Save", width=8, command=save_tasks)
save_btn.grid(row=1, column=0, pady=6)

load_btn = tk.Button(btn_frame, text="Load", width=8, command=load_tasks)
load_btn.grid(row=1, column=1, pady=6)

quit_btn = tk.Button(btn_frame, text="Quit", width=8, command=root.destroy)
quit_btn.grid(row=1, column=2, pady=6)

entry.focus()
root.mainloop()
