import tkinter as tk

# Ablak létrehozása
root = tk.Tk()
root.title("Számológép")
root.geometry("500x600")

# Képernyő (Label), ami megjeleníti az utolsó bevitt számot vagy az eredményt
display = tk.Label(root, text="0", width=16, height=2, anchor="e", font=("Arial", 24))
display.grid(row=0, column=0, columnspan=4)

# Globális változók
current_input = ""  # A jelenlegi szám vagy művelet
operation = ""  # Az aktuális művelet (+, -, *, /)
first_number = None  # Az első szám tárolása a műveletekhez

# Funkciók

# Számgombok kezelésére
def button_click(number):
    global current_input
    if current_input == "0":
        current_input = str(number)
    else:
        current_input += str(number)
    display.config(text=current_input)

# Törlés gomb (Clear)
def clear():
    global current_input, first_number, operation
    current_input = ""
    first_number = None
    operation = ""
    display.config(text="0")

# Művelet kiválasztása (pl. +, -, *, /)
def set_operation(op):
    global first_number, current_input, operation
    if first_number is None:
        first_number = float(current_input)  # Az első szám mentése
        current_input = ""
    operation = op
    display.config(text=current_input)

# Eredmény kiszámítása
def calculate():
    global first_number, current_input, operation
    if operation and first_number is not None:
        second_number = float(current_input)
        if operation == "+":
            result = first_number + second_number
        elif operation == "-":
            result = first_number - second_number
        elif operation == "*":
            result = first_number * second_number
        elif operation == "/":
            if second_number != 0:
                result = first_number / second_number
            else:
                result = "Hiba: 0 osztó"
        display.config(text=str(result))
        first_number = None
        current_input = str(result)
        operation = ""

# Gombok létrehozása

# Szám gombok (0-9, .)
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2),
    ("0", 4, 1)
]

# Műveleti gombok (+, -, *, /)
operations = [
    ("+", 1, 3), ("-", 2, 3), ("*", 3, 3), ("/", 4, 3)
]

# Különleges gombok (Clear, =)
clear_button = tk.Button(root, text="C", width=10, height=2, command=clear)
clear_button.grid(row=4, column=0)

equals_button = tk.Button(root, text="=", width=10, height=2, command=calculate)
equals_button.grid(row=4, column=2)

# Számgombok hozzáadása a gridhez
for (text, row, col) in buttons:
    button = tk.Button(root, text=text, width=10, height=2, command=lambda t=text: button_click(t))
    button.grid(row=row, column=col)

# Műveleti gombok hozzáadása
for (text, row, col) in operations:
    button = tk.Button(root, text=text, width=10, height=2, command=lambda op=text: set_operation(op))
    button.grid(row=row, column=col)

# A Tkinter eseménykezelő indítása
root.mainloop()
