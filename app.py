import tkinter as tk

def click(event):
    button_text = event.widget["text"]
    if button_text == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# Create window
root = tk.Tk()
root.title("Python Calculator")
root.geometry("300x400")

# Entry widget for display
entry = tk.Entry(root, font="Arial 20", justify="right")
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

# Button labels in grid form
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", "C", "=", "+"]
]

# Create button layout
for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for btn in row:
        b = tk.Button(frame, text=btn, font="Arial 18")
        b.pack(side="left", expand=True, fill="both")
        b.bind("<Button-1>", click)

# Start the GUI loop
root.mainloop()
