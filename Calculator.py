import tkinter as tk
from tkinter import ttk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Calculator")
        self.geometry("400x400")
        self.configure(bg="lightblue")
        
        self.expression = ""
        self.input_text = tk.StringVar()
        
        self.create_widgets()
    
    def create_widgets(self):
        # Input field
        input_frame = tk.Frame(self, bg="lightblue")
        input_frame.pack(pady=10)
        
        input_field = ttk.Entry(input_frame, textvariable=self.input_text, font=("Helvetica", 28), justify="right", width=14)
        input_field.grid(row=0, column=0, ipadx=8, ipady=10)
        
        # Buttons
        buttons_frame = tk.Frame(self, bg="lightblue")
        buttons_frame.pack()
        
        buttons = [
            '7', '8', '9', '/', 
            '4', '5', '6', '*', 
            '1', '2', '3', '-', 
            'C', '0', '=', '+'
        ]
        
        row_val = 0
        col_val = 0
        
        for button in buttons:
            action = lambda x=button: self.on_button_click(x)
            tk.Button(buttons_frame, text=button, command=action, width=9, height=3).grid(row=row_val, column=col_val, padx=5, pady=5)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1
    
    def on_button_click(self, button):
        if button == "C":
            self.expression = ""
            self.input_text.set("")
        elif button == "=":
            try:
                result = str(eval(self.expression))
                self.input_text.set(result)
                self.expression = result
            except:
                self.input_text.set("Error")
                self.expression = ""
        else:
            self.expression += button
            self.input_text.set(self.expression)

if __name__ == "__main__":
    calculator = Calculator()
    calculator.mainloop()