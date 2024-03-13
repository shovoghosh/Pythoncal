import tkinter as tk

def on_click(event):
    """Handles button clicks, updating the display or performing operations."""
    global equation
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(equation))
            display_var.set(result)
            equation = result
        except Exception as e:
            display_var.set("Error")
            equation = ""
    elif text == "C":
        equation = ""
        display_var.set(equation)
    else:
        equation += text
        display_var.set(equation)

# Initialize the main window
root = tk.Tk()
root.title("Simple Calculator")

equation = ""
display_var = tk.StringVar()

# Create the display area
display = tk.Entry(root, textvariable=display_var, font=("Arial", 20), bd=10, justify="right")
display.grid(row=0, column=0, columnspan=4)

# Buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# Create and position buttons
for i, button in enumerate(buttons):
    btn = tk.Button(root, text=button, font=("Arial", 20), height=2, width=5)
    btn.grid(row=(i//4)+1, column=i%4)
    btn.bind("<Button-1>", on_click)

# Start the application
root.mainloop()
