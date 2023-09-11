import tkinter as ttk
from tkinter import font
from tkinter import messagebox as mb
app=ttk.Tk()
app.title("Attendance system")
app.geometry('400x400')
font_=font.Font(size=10)



ttk.Label(
    app,
    text='face recognition based attendance system',
    font=font_
).pack()

def register():
    app.destroy()
    with open('opr','w')as f:
        f.write('Register')
    import login_admin


    
def attendance():
    print('Attendance')
    import attendance
    attendance.attendance()
   
def clear_data():
    app.destroy()
    with open('opr','w')as f:
        f.write('clear')
    import login_admin 

    
ttk.Button(app,text='register',command=register,font=font_,height=6,width=15,background='#0033ff').pack(expand=True)
ttk.Button(app,text='Attendance',command=attendance,font=font_,height=6,width=15,background='#0033ff').pack(expand=True)
ttk.Button(app,text='clear_data',command=clear_data,font=font_,height=6,width=15,background='#0033ff').pack(expand=True)





app.mainloop()
            