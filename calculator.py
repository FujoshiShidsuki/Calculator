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
        self.text_input_operations = tk.StringVar()
        self.text_input_answer = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Entry widget for displaying the operations
        self.entry_operations = tk.Entry(self.root, textvariable=self.text_input_operations, font=('arial', 20, 'bold'), bd=20, insertwidth=4, width=14, justify='right')
        self.entry_operations.grid(row=0, column=0, columnspan=4)

        # Entry widget for displaying the answer
        self.entry_answer = tk.Entry(self.root, textvariable=self.text_input_answer, font=('arial', 20, 'bold'), bd=20, insertwidth=4, width=14, justify='right')
        self.entry_answer.grid(row=1, column=0, columnspan=4)

        # Buttons layout
        buttons = [
            ('M+', 2, 0), ('M-', 2, 1), ('MR', 2, 2), ('.', 2, 3),
            ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('/', 3, 3),
            ('4', 4, 0), ('5', 4, 1), ('6', 4, 2), ('*', 4, 3),
            ('1', 5, 0), ('2', 5, 1), ('3', 5, 2), ('-', 5, 3),
            ('0', 6, 0), ('√', 6, 1), ('^', 6, 2), ('+', 6, 3),
            ('AC', 7, 0), ('Del', 7, 1), ('Ans', 7, 2), ('=', 7, 3)
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
            self.update_display()
        elif char == 'Del':
            self.expression = self.expression[:-1]
            self.update_display()
        elif char == 'Ans':
            self.expression += self.last_answer
            self.update_display()
        elif char == '=':
            try:
                result = str(eval(self.expression))
                self.last_answer = result
                self.update_display(answer=result)
                self.expression = result
            except ZeroDivisionError:
                messagebox.showerror("Error", "Division by Zero!")
                self.update_display()
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input!")
                self.update_display()
        elif char == '√':
            try:
                result = str(math.sqrt(eval(self.expression)))
                self.last_answer = result
                self.update_display(answer=result)
                self.expression = result
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input!")
                self.update_display()
        elif char == '^':
            self.expression += '**'
            self.update_display()
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
                self.update_display()
        else:
            self.expression += str(char)
            self.update_display()

    def update_display(self, answer=None):
        self.text_input_operations.set(self.expression)
        if answer is not None:
            self.text_input_answer.set(answer)
        else:
            self.text_input_answer.set("")

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
