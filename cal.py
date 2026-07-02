import tkinter as tk

# สร้างหน้าต่าง
root = tk.Tk()
root.title("เครื่องคิดเลข")
root.geometry("320x450")

expression = ""

# แสดงผล
display = tk.Entry(root, font=("Arial", 20), justify="right")
display.pack(fill="both", padx=10, pady=10, ipady=10)

def press(value):
    global expression
    expression += str(value)
    display.delete(0, tk.END)
    display.insert(tk.END, expression)

def clear():
    global expression
    expression = ""
    display.delete(0, tk.END)

def calculate():
    global expression
    try:
        result = str(eval(expression))
        display.delete(0, tk.END)
        display.insert(tk.END, result)
        expression = result
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")
        expression = ""

# ปุ่มต่าง ๆ
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

frame = tk.Frame(root)
frame.pack(expand=True, fill="both")

for row in buttons:
    row_frame = tk.Frame(frame)
    row_frame.pack(expand=True, fill="both")
    for char in row:
        if char == "=":
            btn = tk.Button(
                row_frame,
                text=char,
                font=("Arial", 18),
                command=calculate
            )
        else:
            btn = tk.Button(
                row_frame,
                text=char,
                font=("Arial", 18),
                command=lambda c=char: press(c)
            )
        btn.pack(side="left", expand=True, fill="both")

# ปุ่มล้าง
tk.Button(
    root,
    text="AC",
    font=("Arial", 18),
    bg="red",
    fg="white",
    command=clear
).pack(fill="both", padx=10, pady=10)

root.mainloop()