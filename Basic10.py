'''
20. File Dialog
21. อ่านข้อมูลจากไฟล์
'''
from tkinter import *
from tkinter.filedialog import *

root = Tk()

#ตั้งค่าหน้าจอ
root.title('โปรแกรมของฉัน')
root.iconbitmap("icons/logo.ico")
root.geometry('300x300+500+200')
root.resizable(0,0)

def selectFile():
    myFile = askopenfilename(title='เปิดไฟล์',initialdir='./', filetypes=(('Text Files','*.txt'),('All Files'))) # ,initialdir='./' เลือกไฟล์ในโปรเจคของเรา
    print(myFile)

    with open(myFile, 'r', encoding='utf-8') as f:
        # print(f.read())
        Label(root, text=f.read()).pack()


btn1 = Button(root, text='เลือกไฟล์', command=selectFile).pack()



root.mainloop()