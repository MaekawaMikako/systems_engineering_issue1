from tkinter import *
from tkmacosx import Button

win = Tk()
win.title('Button practicce')
win.iconbitmap('icon.ico')
win.geometry('550x550')
win.resizable(0,0)
win.config(bg='red')

# ボタンの作成
button_1 = Button(win, text='ボタン1')
button_1.grid(row=0,column=0)

button_2 = Button(win, text='ボタン2')
button_2.grid(row=0,column=1)

button_3 = Button(win, text='ボタン3', bg='pink', activebackground='yellow')
button_3.grid(row=0,column=2, padx=10, pady=10, ipadx=10, ipady=10)

button_4 = Button(win, text='ボタン3', borderwidth=5)
button_4.grid(row=1,column=0, columnspan=3, sticky='WE')

button_5 = Button(win, text='テスト')
button_6 = Button(win, text='テスト')
button_7 = Button(win, text='テスト')
button_8 = Button(win, text='テスト')
button_9 = Button(win, text='テスト')
button_10 = Button(win, text='テスト')

button_5.grid(row=2, column=0, padx=5, pady=5)
button_6.grid(row=2, column=1, padx=5, pady=5)
button_7.grid(row=2, column=2, padx=5, pady=5, sticky='w')
button_8.grid(row=3, column=0, padx=5, pady=5)
button_9.grid(row=3, column=1, padx=5, pady=5)
button_10.grid(row=3, column=2, padx=5, pady=5, sticky='w')

win.mainloop()