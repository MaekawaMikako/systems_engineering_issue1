from tkinter import *
from tkmacosx import *

win = Tk()

win.title('label practice') 
win.iconbitmap('icon.ico') 
win.geometry('550x550') 
win.resizable(0,0) 
win.config(bg='red') # 背景色を赤に設定

# ラベルの作成
label_1 = Label(win, text='よろしくお願いします')
label_1.pack()

label_2 = Label(win, text='よろしくお願いします', font=('Arial', 10, 'bold'))
label_2.pack()

label_3 = Label(win, text='よろしくお願いします', font=('Arial', 10, 'bold'), bg='gray')
label_3.pack(padx=10, pady=10)

label_4 = Label(win, text='よろしくお願いします', font=('Arial', 10, 'bold'), bg='yellow', fg='green')
label_4.pack(padx=10, pady=(0,10), ipadx=50, ipady=50, anchor='w')

label_5 = Label(win, text='よろしくお願いします', font=('Arial', 10, 'bold'), bg='yellow', fg='green')
label_5.pack(padx=10, pady=(0,10), fill='both', expand=True)

win.mainloop()