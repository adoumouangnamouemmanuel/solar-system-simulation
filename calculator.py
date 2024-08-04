# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 14:39:25 2024

@author: emmanuel.adoum
"""

import tkinter as tk


r = tk.Tk()
r.title("Calculator")

def button_add():
    pass

def button_click(number):
    #e.delete(0)
    current = e.get()
    e.delete(0, tk.END)
    e.insert(0, str(current)+str(number))
    
def clear_btn():
    e.delete(0, tk.END)
    
def add_btn():
    val1 = e.get()
    global first_num 
    first_num = int(val1)
    e.delete(0, tk.END)

def equal_btn():
    second = e.get()
    s = first_num + int(second)
    e.delete(0, tk.END)
    e.insert(0, s)
    
    
    

e = tk.Entry(r, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10,
       pady=10)

btn1 = tk.Button(r, text='1', padx=40, pady=20,
                 command=lambda: button_click(1))

btn2 = tk.Button(r, text='2', padx=40, pady=20,
                 command=lambda: button_click(2))

btn3 = tk.Button(r, text='3', padx=40, pady=20,
                 command=lambda: button_click(3))

btn4 = tk.Button(r, text='4', padx=40, pady=20,
                 command=lambda: button_click(4))

btn5 = tk.Button(r, text='5', padx=40, pady=20,
                 command=lambda: button_click(5))

btn6 = tk.Button(r, text='6', padx=40, pady=20,
                 command=lambda: button_click(6))

btn7 = tk.Button(r, text='7', padx=40, pady=20,
                 command=lambda: button_click(7))

btn8 = tk.Button(r, text='8', padx=40, pady=20,
                 command=lambda: button_click(8))

btn9 = tk.Button(r, text='9', padx=40, pady=20,
                 command=lambda: button_click(9))

btn0 = tk.Button(r, text='0', padx=40, pady=20,
                 command=lambda: button_click(0))


btn_add = tk.Button(r, text='+', padx=39, pady=20,
                 command=add_btn)

btn_equal = tk.Button(r, text='=', padx=91, pady=20,
                 command=equal_btn)

btn_clear = tk.Button(r, text='Clear', padx=79, pady=20,
                 command=clear_btn)


# Put buttons on screens
btn1.grid(row=3, column=0)
btn2.grid(row=3, column=1)
btn3.grid(row=3, column=2)

btn4.grid(row=2, column=0)
btn5.grid(row=2, column=1)
btn6.grid(row=2, column=2)

btn7.grid(row=1, column=0)
btn8.grid(row=1, column=1)
btn9.grid(row=1, column=2)

btn0.grid(row=4, column=0)


btn_add.grid(row=5, column=0)
btn_clear.grid(row=4, column=1, columnspan=2)
btn_equal.grid(row=5, column=1, columnspan=2)

r.mainloop()
