import tkinter as tk

# Ablak létrehozása
root = tk.Tk()
root.title("Számológép")    #ablak elnevezése
root.geometry("350x250")    #ablak mérete

# Label, ami mutatja az utolsó bevitt számot vagy az eredményt
display = tk.Label(root,text="0",width=16,height=2,anchor="e",font=("Arial",24))
display.grid(row=0,column=0,columnspan=4)

# Globális változók
current_input = ""  # A jelenlegi szám vagy művelet
muvelet = ""  # Az aktuális művelet (+, -, *, /)
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
    global current_input, first_number, muvelet
    current_input = ""
    first_number = None
    muvelet = ""
    display.config(text="0")

# Művelet kiválasztása (pl. +, -, *, /)
def set_operation(muv):
    global first_number, current_input, muvelet
    if first_number is None:
        first_number = float(current_input)  # Az első szám mentése
        current_input = ""
    muvelet = muv
    display.config(text=current_input)

# Eredmény kiszámítása
def calculate():
    global first_number, current_input, muvelet
    if muvelet and first_number is not None:
        second_number = float(current_input)
        if muvelet == "+":
            result = first_number + second_number   #összeadás
        elif muvelet == "-":
            result = first_number - second_number   #kivonás
        elif muvelet == "*":
            result = first_number * second_number   #szorzás
        elif muvelet == "/":
            if second_number != 0:
                result = first_number / second_number   #osztás
            else:
                result = "Hiba: 0 osztó"    #0-val osztás nem lehet
        display.config(text=str(result))
        first_number = None
        current_input = str(result)
        muvelet = ""

# Gombok létrehozása

# Szám gombok (0-9)
buttons = [
    ("7",1,0),("8",1,1),("9",1,2),
    ("4",2,0),("5",2,1),("6",2,2),
    ("1",3,0),("2",3,1),("3",3,2),
    ("0",4,1)
]

# Műveleti gombok (+, -, *, /)
muveletek = [("+",1,3),("-",2,3),("*",3,3),("/",4,3)]

# Különleges gombok (Clear, =)
c_button = tk.Button(root, text="C", width=10, height=2, command=clear)
c_button.grid(row=4, column=0)

eredm_button = tk.Button(root, text="=", width=10, height=2, command=calculate)
eredm_button.grid(row=4, column=2)

# Számgombok hozzáadása a gridhez
for (text, row, col) in buttons:
    button = tk.Button(root, text=text, width=10, height=2, command=lambda szam=text: button_click(szam))
    button.grid(row=row, column=col)

# Műveleti gombok hozzáadása
for (text, row, col) in muveletek:
    button = tk.Button(root, text=text, width=10, height=2, command=lambda muv=text: set_operation(muv))
    button.grid(row=row, column=col)

# A Tkinter eseménykezelő indítása
root.mainloop()