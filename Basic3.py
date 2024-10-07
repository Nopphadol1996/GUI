from tkinter import *

root = Tk()

#ตั้งค่าหน้าจอ
root.title('โปรแกรมของฉัน')
root.iconbitmap("icons/logo.ico")
root.geometry('300x300+500+200')
root.resizable(0,0)
root.config(bg='pink')

#แสดงข้อความ
'''

label1=Label(root)
label1.config(text='สวัสดี')
label1.config(font=('Angsana New',30,'bold'))
label1.config(bg='red')
label1.config(fg='white')
label1.pack()

'''
# เขียนคำสั่งย่อ
label1=Label(root,text='สวัสดี',font=('Angsana New',30,'bold'),bg='red',fg='white')
label1.pack()

label2=Label(root,text='Python',font=('Angsana New',30,'bold'),bg='blue',fg='white')
label2.pack()

label3=Label(root,text='Tkinter',font=('Angsana New',30,'bold'),bg='green',fg='white')
label3.pack()

label4=Label(root,text='GUI',font=('Angsana New',30,'bold'),bg='black',fg='white')
label4.pack()


root.mainloop()