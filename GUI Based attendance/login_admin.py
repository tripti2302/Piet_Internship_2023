import tkinter as ttk
from tkinter import font
from tkinter import messagebox as mb

login_app=ttk.Tk()
login_app.geometry('400x400')
login_app.title('Login Data')
font_=font.Font(size=10)

ttk.Label(login_app,text='Enter Your Credentials',font=font_).pack()

uname=ttk.Variable(login_app)
pwd=ttk.Variable(login_app)
ttk.Label(login_app,text='User Name',font=font_).place(x=100,y=80)
ttk.Entry(login_app,font=font_,textvariable=uname).place(x=250,y=80)

ttk.Label(login_app,text='Password',font=font_).place(x=100,y=130)
ttk.Entry(login_app,font=font_,show='#',textvariable=pwd).place(x=250,y=130)

def submit():
    op =''
    with open('opr','r') as f:
        op=f.read()
        print(op)
    if len(op)>0:
        userid=uname.get()
        password=pwd.get()
        p=open('pwd').read()
        uname.set('')
        pwd.set('')
        if userid=='admin' and password==p:
            print('login successful')
            mb.showinfo('Success','login successful')
            login_app.destroy()
            from tkinter.simpledialog import askstring
            name=askstring('Name','for whom you want to register?')
            import register as rt
            rt.register(name)
        elif op=='clear':
            import clear_data    
            
    else:
         print('login failed')
         mb.showerror('Error','Login failed')
    

def back():
    login_app.destroy()
    with open('opr','w') as f:
        f.write('')
    import app

ttk.Button(login_app,text='Submit',command=submit,font=font_,height=1,width=7,bg='#3498DB').place(x=350,y=180)

ttk.Button(login_app,text='Back',command=back,font=font_,height=1,width=7,bg='#3498DB').place(x=350,y=250)

login_app.mainloop()