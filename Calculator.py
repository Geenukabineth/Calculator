from tkinter import Tk, Entry, Button, StringVar

class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry('357x420+0+0')
        master.config(bg='gray')
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ''
        Entry(width=17, bg='#fff', font=('Arial Bold', 28), textvariable=self.equation).place(x=0, y=0)

        button_width = 12
        button_height = 5

        Button(master, text='C', width=button_width, height=button_height, command=self.clear).place(x=0, y=50)
        Button(master, text='/', width=button_width, height=button_height, command=lambda: self.show('/')).place(x=90, y=50)
        Button(master, text='*', width=button_width, height=button_height, command=lambda: self.show('*')).place(x=180, y=50)
        Button(master, text='-', width=button_width, height=button_height, command=lambda: self.show('-')).place(x=270, y=50)

        Button(master, text='7', width=button_width, height=button_height, command=lambda: self.show(7)).place(x=0, y=125)
        Button(master, text='8', width=button_width, height=button_height, command=lambda: self.show(8)).place(x=90, y=125)
        Button(master, text='9', width=button_width, height=button_height, command=lambda: self.show(9)).place(x=180, y=125)
        Button(master, text='+', width=button_width, height=button_height, command=lambda: self.show('+')).place(x=270, y=125)

        Button(master, text='4', width=button_width, height=button_height, command=lambda: self.show(4)).place(x=0, y=200)
        Button(master, text='5', width=button_width, height=button_height, command=lambda: self.show(5)).place(x=90, y=200)
        Button(master, text='6', width=button_width, height=button_height, command=lambda: self.show(6)).place(x=180, y=200)
        Button(master, text='=', width=button_width, height=button_height*3, command=self.solve).place(x=270, y=200)

        Button(master, text='1', width=button_width, height=button_height, command=lambda: self.show(1)).place(x=0, y=275)
        Button(master, text='2', width=button_width, height=button_height, command=lambda: self.show(2)).place(x=90, y=275)
        Button(master, text='3', width=button_width, height=button_height, command=lambda: self.show(3)).place(x=180, y=275)

        Button(master, text='0', width=button_width*2, height=button_height, command=lambda: self.show(0)).place(x=0, y=350)
        Button(master, text='.', width=button_width, height=button_height, command=lambda: self.show('.')).place(x=180, y=350)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            result = eval(self.entry_value)
            self.equation.set(result)
            self.entry_value = str(result)
        except:
            self.equation.set("Error")
            self.entry_value = ""

root = Tk()
calculator = Calculator(root)
root.mainloop()
