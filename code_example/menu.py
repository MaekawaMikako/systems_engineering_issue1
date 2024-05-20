from tkinter import *
from tkmacosx import *

# ウィンドウの作成
root = Tk()
root.title('Menu Practice!')
root.geometry('300x200')
root.resizable(0, 0)


# 関数の作成
def open_setting():
    subwindow = Toplevel()
    subwindow.title('設定')
    subwindow.geometry('200x100+500+150')

    subwindow_label = Label(subwindow, text='設定画面です')
    subwindow_label.pack(pady=30)


# メニューバーの作成
# メニューバーの親となるコンテナの作成
menubar = Menu(root)
root.config(menu=menubar)

# 設定メニューの作成
setting_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='設定', menu=setting_menu)

# ファイルメニューの作成
file_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='ファイル', menu=file_menu)

# 設定メニューにプルダウンメニューを追加
setting_menu.add_command(label='環境設定', command=open_setting)
setting_menu.add_command(label='終了')

# ファイルメニューにプルダウンメニューを追加
file_menu.add_command(label='新規ファイル')


# ボタンの作成
button_1 = Button(root, text='テスト')
button_1.grid(row=0, column=0, padx=100, pady=70, ipadx=10)


# ループ処理
root.mainloop()
