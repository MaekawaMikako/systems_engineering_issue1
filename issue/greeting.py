from tkinter import *
import tkinter as t

def func(event):
    s = ent.get()
    lab[ 'text' ] = s
    ent.delete( 0, t.END )

# ウィンドウの作成
window = Tk()
window.title('window practice') # ウィンドウタイトルの設定
window.iconbitmap('icon.ico') # .icoの拡張子の画像のみ使用可能(Macでは使用不可)
window.geometry('300x800') # ウィンドウサイズの設定(横300x縦800pix)
window.resizable(0,0) # 横、縦ともにサイズ変更禁止
# window.resizable(0,1) # 横はサイズ変更禁止、縦はサイズ変更可能
# window.resizable(1,1) # 横、縦ともにサイズ変更可能
window.config(bg='gray') # 背景色を灰色に設定

ent = t.Entry(background='white', foreground = 'black')
ent.place(x = 10, y = 20)

but = t.Button(text = '実行')
but.place(x = 10, y = 55, width = 230, height = 25)
but.bind('<Button-1>', func)

lab = t.Label( background = 'white', foreground = 'black')
lab.place( x = 10, y = 100, width = 230, height = 25 )

# ウィンドウのループ処理
window.mainloop()
