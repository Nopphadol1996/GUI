'''
14. Entry Widget
15.command Callback
16. Text variable
17. message box
18.Quit program
'''
from tkinter import *
import tkinter.messagebox

root = Tk()

#ตั้งค่าหน้าจอ
root.title('โปรแกรมของฉัน')
root.iconbitmap("icons/logo.ico")
root.geometry('300x300+500+200')
root.resizable(0,0)

def quitProgram():
    confirm = tkinter.messagebox.askquestion('ยืนยัน', 'คุณต้องการปิดโปรแกรมหรือไม่ ?')
    print(confirm)
    if confirm == 'yes':
        root.destroy()

def showName():
    name = username.get()
    if name == '':
        tkinter.messagebox.showerror('เกิดข้อผิดพลาด', 'กรุณาป้อนข้อมูล ' + name)
    
    else:

        myText.delete(0,END) # delete ข้อความในช่อง Entry
        tkinter.messagebox.showinfo('รายละเอียด', 'ผู้ใช้งานโปรแกรมคือ ' + name)

username = StringVar() # ส่วนที่เก็บข้อมูลใน Entry widget
myText = Entry(root, width=40, font=('Arial',25), textvariable=username)
myText.pack(padx=10,pady=10)
btnSave = Button(root, text='บันทึก', fg='white', bg='blue', command=showName)
btnSave.pack(ipadx=30, ipady=10)

btnQuit = Button(root, text='ออกจากโปรแกรม', fg='white', bg='purple', command=quitProgram)
btnQuit.pack(ipadx=30, ipady=10, pady=5)

root.mainloop()