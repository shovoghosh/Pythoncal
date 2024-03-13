import tkinter as tk

def convert_temperature():
    """Converts temperature between Celsius and Fahrenheit and displays the result."""
    temp = temp_entry.get()
    if temp.isdigit() or (temp.startswith('-') and temp[1:].isdigit()):
        temp = float(temp)
        if var.get() == 1:
            # Convert Celsius to Fahrenheit
            result = (temp * 9/5) + 32
            result_label.config(text=f"{temp} Celsius is {result:.2f} Fahrenheit")
        else:
            # Convert Fahrenheit to Celsius
            result = (temp - 32) * 5/9
            result_label.config(text=f"{temp} Fahrenheit is {result:.2f} Celsius")
    else:
        result_label.config(text="Please enter a valid number.")

# Initialize the main window
root = tk.Tk()
root.title("Temperature Converter")
root.config(bg="#ddf")

# Frames for layout
input_frame = tk.Frame(root, bg="#ddf")
input_frame.pack(pady=20)

output_frame = tk.Frame(root, bg="#ddf")
output_frame.pack(pady=10)

# Entry widget for temperature
temp_entry = tk.Entry(input_frame, font=("Arial", 16), width=10)
temp_entry.grid(row=0, column=1, padx=10)

# Label for entry widget
temp_label = tk.Label(input_frame, text="Enter Temperature:", font=("Arial", 16), bg="#ddf")
temp_label.grid(row=0, column=0)

# Radio buttons for unit selection
var = tk.IntVar()
celsius_rb = tk.Radiobutton(input_frame, text="Celsius to Fahrenheit", variable=var, value=1, font=("Arial", 12), bg="#ddf")
celsius_rb.grid(row=1, column=0, pady=10)
fahrenheit_rb = tk.Radiobutton(input_frame, text="Fahrenheit to Celsius", variable=var, value=2, font=("Arial", 12), bg="#ddf")
fahrenheit_rb.grid(row=1, column=1)
var.set(1)

# Convert button
convert_button = tk.Button(input_frame, text="Convert", command=convert_temperature, font=("Arial", 16), bg="#acc")
convert_button.grid(row=2, column=0, columnspan=2, pady=10)

# Label to display the result
result_label = tk.Label(output_frame, text="", font=("Arial", 16), bg="#ddf")
result_label.pack()

root.mainloop()
