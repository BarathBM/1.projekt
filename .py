import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Egyszerű számológép")
        self.geometry("400x500")
        
        self.current_input = ""
        self.previous_input = ""
        self.operation = None
        
        self.create_widgets()

    def create_widgets(num):
        # Kijelző (Label)
        num.result_label = tk.Label(num, text="", height=2, font=("Arial", 24), anchor="e", padx=10)
        num.result_label.grid(row=0, column=0, columnspan=4)

        # Számgombok
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
            ('0', 4, 1)
        ]
        
        for (text, row, col) in buttons:
            button = tk.Button(self, text=text, font=("Arial", 18), width=5, height=2,
                               command=lambda t=text: self.append_number(t))
            button.grid(row=row, column=col)

        # Művelet gombok
        operations = [
            ('+', 1, 3), ('-', 2, 3), ('*', 3, 3), ('/', 4, 3)
        ]
        
        for (text, row, col) in operations:
            button = tk.Button(self, text=text, font=("Arial", 18), width=5, height=2,
                               command=lambda t=text: self.set_operation(t))
            button.grid(row=row, column=col)

        # Egyenlőség gomb
        equals_button = tk.Button(self, text="=", font=("Arial", 18), width=5, height=2,
                                  command=self.calculate)
        equals_button.grid(row=4, column=2)

        # Clear gomb
        clear_button = tk.Button(self, text="C", font=("Arial", 18), width=5, height=2,
                                 command=self.clear)
        clear_button.grid(row=4, column=0)

    def append_number(self, num):
        self.current_input += num
        self.update_display()

    def set_operation(self, operation):
        if self.current_input:
            self.previous_input = self.current_input
            self.current_input = ""
            self.operation = operation
            self.update_display()

    def update_display(self):
        display_text = self.current_input if not self.operation else f"{self.previous_input} {self.operation} {self.current_input}"
        self.result_label.config(text=display_text)

    def calculate(self):
        try:
            if self.previous_input and self.current_input:
                result = eval(f"{self.previous_input} {self.operation} {self.current_input}")
                self.result_label.config(text=str(result))
                self.previous_input = str(result)
                self.current_input = ""
                self.operation = None
        except ZeroDivisionError:
            self.result_label.config(text="Hiba: Osztás 0-val!")
            self.current_input = ""
            self.operation = None

    def clear(self):
        self.current_input = ""
        self.previous_input = ""
        self.operation = None
        self.update_display()

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()