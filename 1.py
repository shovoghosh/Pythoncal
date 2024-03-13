import tkinter as tk
from tkinter import messagebox

def show_message():
    """Function to display a message."""
    messagebox.showinfo("Message", "Hello, Tkinter!")

# Create the main window
root = tk.Tk()
root.title("Simple Tkinter App")
root.geometry("300x200")  # Set the size of the window

# Create a button widget
btn_show_message = tk.Button(root, text="Click Me", command=show_message)
btn_show_message.pack(pady=20)  # Add some padding for aesthetics

# Run the application
root.mainloop()
