from tkinter import *
import tkinter
import tkinter as t
import tkinter as tk

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
window.title('window practice') # ウィンドウタイトルの設定
window.iconbitmap('icon.ico') # .icoの拡張子の画像のみ使用可能(Macでは使用不可)
window.geometry('300x300') # ウィンドウサイズの設定(横300x縦800pix)
window.resizable(0,0) # 横、縦ともにサイズ変更禁止
window.config(bg='gray') # 背景色を灰色に設定

ent = t.Entry(background='white', foreground = 'black')
ent.grid(row=0,column=0)

#ラジオボタンのラベルをリスト化する
radio_text = ['朝', '昼', '夜']

#ラジオボタンの状態
radio_var = tkinter.IntVar()

#ラジオボタンを動的に作成して設置
for i in range(len(radio_text)):
    radio = tkinter.Radiobutton(window, value=i, variable=radio_var, text=radio_text[i])
    radio.grid(row=1,column=i)

but = t.Button(text = '実行')
but.bind('<Button-1>', func)
but.grid(row=0,column=1)

lab = t.Label( background = 'white', foreground = 'black')
lab.place(x = 10, y = 100, width = 230, height = 250 )

# ウィンドウのループ処理
window.mainloop()
