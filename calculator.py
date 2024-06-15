import tkinter as tk
from tkinter import messagebox
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        self.expression = ""
        self.last_answer = ""
        self.memory = None  # Memory variable
        self.text_input = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Entry widget for displaying the expression
        self.entry = tk.Entry(self.root, textvariable=self.text_input, font=('arial', 20, 'bold'), bd=20, insertwidth=4, width=14, justify='right')
        self.entry.grid(row=0, column=0, columnspan=4)

        # Buttons layout
        buttons = [
            ('M+', 1, 0), ('M-', 1, 1), ('MR', 1, 2), ('/', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
            ('0', 5, 0), ('√', 5, 1), ('^', 5, 2), ('.', 5, 3),
            ('AC', 6, 0), ('Del', 6, 1), ('Ans', 6, 2), ('=', 6, 3)
        ]

        button_width = 4
        button_height = 2  # Adjust height to match your desired dimensions

        for (text, row, col) in buttons:
            self.create_button(text, row, col, width=button_width, height=button_height)

    def create_button(self, text, row, col, width, height):
        button = tk.Button(self.root, text=text, padx=10, pady=10, bd=8, fg="black", font=('arial', 18, 'bold'),
                           width=width, height=height,
                           command=lambda t=text: self.on_button_click(t))
        button.grid(row=row, column=col)

    def on_button_click(self, char):
        if char == 'AC':
            self.expression = ""
            self.last_answer = ""
            self.text_input.set(self.expression)
        elif char == 'Del':
            self.expression = self.expression[:-1]
            self.text_input.set(self.expression)
        elif char == 'Ans':
            self.expression += self.last_answer
            self.text_input.set(self.expression)
        elif char == '=':
            try:
                result = str(eval(self.expression))
                self.last_answer = result
                self.text_input.set(result)
                self.expression = result
            except ZeroDivisionError:
                messagebox.showerror("Error", "Division by Zero!")
                self.text_input.set("")
                self.expression = ""
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input!")
                self.text_input.set("")
                self.expression = ""
        elif char == '√':
            try:
                result = str(math.sqrt(eval(self.expression)))
                self.last_answer = result
                self.text_input.set(result)
                self.expression = result
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input!")
                self.text_input.set("")
                self.expression = ""
        elif char == '^':
            self.expression += '**'
            self.text_input.set(self.expression)
        elif char == 'M+':  # Memory add
            try:
                self.memory = eval(self.expression)
                messagebox.showinfo("Memory", f"Stored: {self.memory}")
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input!")
        elif char == 'M-':  # Memory subtract
            try:
                self.memory -= eval(self.expression)
                messagebox.showinfo("Memory", f"Stored: {self.memory}")
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input!")
        elif char == 'MR':  # Memory recall
            if self.memory is not None:
                self.expression += str(self.memory)
                self.text_input.set(self.expression)
        else:
            self.expression += str(char)
            self.text_input.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
