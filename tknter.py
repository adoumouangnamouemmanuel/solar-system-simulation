# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 23:54:47 2024.

@author: emmanuel.adoum
"""

import tkinter as tk

w = tk.Tk()
# w.config(font = (("Times New Roman"),15), bg='yellow')

w.title("Emma GUI")
icon = tk.PhotoImage(file='logo-red-zamigo-copy-size.png')
w.iconphoto(True, icon)
w.geometry('600x600')


e = tk.Entry(w, width=30, font = (("Times New Roman"),15))
e.grid(row=0, column=0)

def func():
    lab = tk.Label(w, text=e.get(), font = (("Times New Roman"),15))
    lab.grid(row=2, column=0)

btn = tk.Button(w, padx=50,fg='red', 
                command=func, text="Enter your name",
                font = (("Times New Roman"),15))
btn.grid(row=0, column=1)



w.mainloop()