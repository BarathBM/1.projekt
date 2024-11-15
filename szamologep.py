import tkinter as tk

# Ablak létrehozása
root = tk.Tk()
root.title("Számológép")    #ablak elnevezése
root.geometry("500x350")    #ablak mérete

# Label, ami mutatja az utolsó bevitt számot vagy az eredményt
kep = tk.Label(root, text="0", width=16, height=2, anchor="e", font=("Arial", 24))
kep.grid(row=0, column=0, columnspan=4)

# Globális változók
input = ""  # A jelenlegi szám vagy művelet
muvelet = ""  # Az aktuális művelet (+, -, *, /)
elsoszam = None  # Az első szám tárolása a műveletekhez

# Funkciók

# Számgombok kezelésére
def button_click(number):
    global input
    if input == "0":
        input = str(number)  # Ha a kijelző 0, akkor a következő szám kerül rá
    else:
        input += str(number)  # A már meglévő számhoz hozzáadjuk az új számot
    kep.config(text=input)  # Frissítjük a kijelzőt

# Törlés gomb (Clear)
def clear():
    global input, elsoszam, muvelet
    input = ""  # Töröljük az aktuális inputot
    elsoszam = None  # Nincs tárolt szám
    muvelet = ""  # Nincs művelet
    kep.config(text="0")  # A kijelzőn "0" lesz

# Művelet kiválasztása (pl. +, -, *, /)
def set_operation(muv):
    global elsoszam, input, muvelet
    if elsoszam is None:
        elsoszam = int(input)  # Az első szám mentése
        input = ""  # Az inputot kiürítjük a következő szám bevitelére
    muvelet = muv  # A műveletet tároljuk el
    kep.config(text=input + " " + muv)  # A kijelzőn a művelet is látható legyen

# Eredmény kiszámítása
def calculate():
    global elsoszam, input, muvelet
    if muvelet and elsoszam is not None:  # Ha van művelet és van első szám
        masodikszam = int(input)  # A második szám, amit a felhasználó beírt
        if muvelet == "+":
            eredmeny = elsoszam + masodikszam  # összeadás
        elif muvelet == "-":
            eredmeny = elsoszam - masodikszam  # kivonás
        elif muvelet == "*":
            eredmeny = elsoszam * masodikszam  # szorzás
        elif muvelet == "/":
            if masodikszam != 0:
                eredmeny = elsoszam / masodikszam  # osztás
            else:
                eredmeny = "Hiba: 0 osztó"  # 0-val való osztás nem engedélyezett
        kep.config(text=str(eredmeny))  # Az eredményt megjelenítjük a kijelzőn
        elsoszam = None  # Töröljük az első számot
        input = str(eredmeny)  # Az inputot az eredményre állítjuk
        muvelet = ""  # A műveletet töröljük

# Gombok létrehozása

# Szám gombok (0-9)
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2),
    ("0", 4, 1)
]

# Műveleti gombok (+, -, *, /)
muveletek = [("+", 1, 3), ("-", 2, 3), ("*", 3, 3), ("/", 4, 3)]

# Különleges gombok (Clear, =)
c_button = tk.Button(root, text="C", width=15, height=3, command=clear)
c_button.grid(row=4, column=0)

eredm_button = tk.Button(root, text="=", width=15, height=3, command=calculate)
eredm_button.grid(row=4, column=2)

# Számgombok hozzáadása a gridhez
for (text, row, col) in buttons:
    button = tk.Button(root, text=text, width=15, height=3, command=lambda szam=text: button_click(szam))
    button.grid(row=row, column=col)

# Műveleti gombok hozzáadása
for (text, row, col) in muveletek:
    button = tk.Button(root, text=text, width=15, height=3, command=lambda muv=text: set_operation(muv))
    button.grid(row=row, column=col)

# A Tkinter eseménykezelő indítása
root.mainloop()
