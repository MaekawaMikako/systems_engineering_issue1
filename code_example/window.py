from tkinter import *

# ウィンドウの作成
window = Tk()
window.title('window practice') # ウィンドウタイトルの設定
window.iconbitmap('icon.ico') # .icoの拡張子の画像のみ使用可能(Macでは使用不可)
window.geometry('300x800') # ウィンドウサイズの設定(横300x縦800pix)
window.resizable(0,0) # 横、縦ともにサイズ変更禁止
# window.resizable(0,1) # 横はサイズ変更禁止、縦はサイズ変更可能
# window.resizable(1,1) # 横、縦ともにサイズ変更可能
window.config(bg='red') # 背景色を赤に設定

# サブウィンドウの作成
subwin = Toplevel()
subwin.title('Second window')
subwin.config(bg='#123123') # 色の設定としてカラーコードが設定可能
subwin.geometry('200x300+500+500') # 横500, 縦500ずれた場所にウィンドウを配置

# ウィンドウのループ処理
window.mainloop()


