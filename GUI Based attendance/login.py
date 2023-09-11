import tkinter as ttk
from tkinter import font
login_app=ttk.Tk()
login_app.title('Login Page')
login_app.geometry('800x800')
login_app.grid_columnconfigure(0,weight=2)
font_=font.Font(size=14)


ttk.Label(
    login_app,
    text='Enter the Credentials',
    font=font_
).grid(row=0,column=1)

ttk.Label(login_app,text='Username').grid(row=5,column=1,pady=0.2)
ttk.Entry(login_app,font=font_).grid(row=5,column=2,pady=0.2)


ttk.Label(login_app,text='Password').grid(row=6,column=1,pady=0.2)
ttk.Entry(login_app,font=font_).grid(row=6,column=2,pady=0.2)























login_app.mainloop()