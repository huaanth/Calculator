import tkinter as tk
calc = ""

def calc_input(symbol):
    global calc
    calc += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calc)

def eval_calc ():
    global calc
    try:
        calc = str(eval(calc)) #allows me to calculate inputs
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calc)
    except:
        clear_calc()
        text_result.insert(1.0, "Error")
    pass

def clear_calc ():
    global calc
    calc = ""
    text_result.delete(1.0, "end")
    pass

root = tk.Tk() #creating the object

root.geometry("310x250") #dimensions

text_result = tk.Text(root, height =2, width =12, font=("Arial", 24)) #text dimensions
text_result.grid(columnspan=5)
#next few lines are for the butons
btn_1 = tk.Button(root, text = "1", command = lambda: calc_input(1), width = 5, font = ("Arial", 14))
btn_1.grid(row = 2, column =1)
btn_2 = tk.Button(root, text = "2", command = lambda: calc_input(2), width = 5, font = ("Arial", 14))
btn_2.grid(row = 2, column =2)
btn_3 = tk.Button(root, text = "3", command = lambda: calc_input(3), width = 5, font = ("Arial", 14))
btn_3.grid(row = 2, column =3)
btn_4 = tk.Button(root, text = "4", command = lambda: calc_input(4), width = 5, font = ("Arial", 14))
btn_4.grid(row = 3, column =1)
btn_5 = tk.Button(root, text = "5", command = lambda: calc_input(5), width = 5, font = ("Arial", 14))
btn_5.grid(row = 3, column =2)
btn_6 = tk.Button(root, text = "6", command = lambda: calc_input(6), width = 5, font = ("Arial", 14))
btn_6.grid(row = 3, column =3)
btn_7 = tk.Button(root, text = "7", command = lambda: calc_input(7), width = 5, font = ("Arial", 14))
btn_7.grid(row = 4, column =1)
btn_8 = tk.Button(root, text = "8", command = lambda: calc_input(8), width = 5, font = ("Arial", 14))
btn_8.grid(row = 4, column =2)
btn_9 = tk.Button(root, text = "9", command = lambda: calc_input(9), width = 5, font = ("Arial", 14))
btn_9.grid(row = 4, column =3)
btn_0 = tk.Button(root, text = "0", command = lambda: calc_input(0), width = 5, font = ("Arial", 14))
btn_0.grid(row = 5, column =2)

btn_plus = tk.Button(root, text = "+", command = lambda: calc_input("+"), width = 5, font = ("Arial", 14))
btn_plus.grid(row = 2, column =4)
btn_sub = tk.Button(root, text = "-", command = lambda: calc_input("-"), width = 5, font = ("Arial", 14))
btn_sub.grid(row = 3, column =4)
btn_mul = tk.Button(root, text = "*", command = lambda: calc_input("*"), width = 5, font = ("Arial", 14))
btn_mul.grid(row = 4, column =4)
btn_divide = tk.Button(root, text = "÷", command = lambda: calc_input("/"), width = 5, font = ("Arial", 14))
btn_divide.grid(row = 5, column =4)
btn_open = tk.Button(root, text = "(", command = lambda: calc_input("("), width = 5, font = ("Arial", 14))
btn_open.grid(row = 5, column =1)
btn_close = tk.Button(root, text = ")", command = lambda: calc_input(")"), width = 5, font = ("Arial", 14))
btn_close.grid(row = 5, column =3)
btn_equals = tk.Button(root, text = "=", command = eval_calc, width = 15, font = ("Arial", 14))
btn_equals.grid(row = 6, column =3, columnspan=2)
btn_clear = tk.Button(root, text = "C", command = clear_calc, width = 15, font = ("Arial", 14))
btn_clear.grid(row = 6, column =1, columnspan=2)
root.mainloop() #runs the object
