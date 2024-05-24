from tkinter import *
import tkinter
import tkinter as t
import tkinter as tk
from PIL import ImageTk, Image

text  = ""
def func(event):
    s = ent.get()
    num = radio_var.get()
    if(radio_text[num] == "朝"):
        lab[ 'text' ] += "\nおはようございます！" + s + "さん"
    elif(radio_text[num] == "昼"):
        lab[ 'text' ] += "\nこんにちは！" + s + "さん"
    elif(radio_text[num] == "夜"):
        lab[ 'text' ] += "\nこんばんは！" + s + "さん"
    ent.delete( 0, t.END )

# ウィンドウの作成
window = Tk()
window.title('あいさつアプリ') # ウィンドウタイトルの設定
window.iconbitmap('icon.ico') # .icoの拡張子の画像のみ使用可能(Macでは使用不可)
window.geometry('500x500') # ウィンドウサイズの設定(横300x縦800pix)
window.resizable(0,0) # 横、縦ともにサイズ変更禁止
window.config(bg='gray85') # 背景色を灰色に設定

# StringVarクラスのインスタンス生成
entry_text = StringVar(window)
# インスタンスに文字列をセット
entry_text.set('')

ent = t.Entry(bg='white', foreground = 'black', width=44, textvariable=entry_text, highlightbackground="skyblue")
ent.grid(padx=18, pady=30)
ent.bind("<Return>", func)

#ラジオボタンのラベルをリスト化する
radio_text = ['朝', '昼', '夜']

#ラジオボタンの状態
radio_var = tkinter.IntVar()

#ラジオボタンを動的に作成して設置
for i in range(len(radio_text)):
    radio = tkinter.Radiobutton(window, value=i+2, variable=radio_var, text=radio_text[i])
    radio.place(x = 70+140*i, y = 70)
    radio.config(bd=0, bg='gray85', fg='black')

img = PhotoImage(file='submit.png')
but = Button(image=img)
but.bind('<Button-1>', func)
but.grid(row=0,column=1)
but.config(bd=0)

lab = tk.Label( bg = 'gray55', foreground = 'black', anchor=tk.N)
lab.place(x = 10, y = 110, width = 480, height = 380 )

# ウィンドウのループ処理
window.mainloop()
