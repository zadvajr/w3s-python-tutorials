import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        
        # Entry widget to display expressions
        self.entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief='solid')
        self.entry.grid(row=0, column=0, columnspan=4)
        
        # Buttons for digits and operations
        self.create_buttons()
        
    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/', 
            '4', '5', '6', '*', 
            '1', '2', '3', '-', 
            '0', '.', '=', '+'
        ]
        
        row = 1
        col = 0
        
        for button in buttons:
            button_command = lambda x=button: self.on_button_click(x)
            tk.Button(self.root, text=button, width=5, height=2, font=('Arial', 18), command=button_command).grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1
        
        # Clear button
        tk.Button(self.root, text='C', width=5, height=2, font=('Arial', 18), command=self.clear_entry).grid(row=row, column=0, columnspan=4, sticky='nsew')
        
    def on_button_click(self, char):
        if char == '=':
            try:
                expression = self.entry.get()
                result = eval(expression)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, 'Error')
        else:
            current_text = self.entry.get()
            new_text = current_text + char
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, new_text)
    
    def clear_entry(self):
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
