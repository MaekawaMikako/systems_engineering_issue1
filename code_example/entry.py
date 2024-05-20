from tkinter import *
from tkinter.constants import END
from tkmacosx import *


def print_text(): # 引数のない関数
    text = Label(frame_2, text=entry_1.get()) # entry_1に入力された文字列をframe2にラベルとして配置
    text.pack()

    entry_1.delete(0, END) # entry_1の文字列の0からENDまでを消去


def count(number): # 引数のある関数
    global value

    text = Label(frame_2, text=number, bg='#499499')
    text.pack()

    value = number + 1


# ウィンドウの作成
root = Tk()
root.title('Entry practice!')
root.iconbitmap('icon.ico')
root.geometry('550x550')
root.resizable(0, 0)

# frameの作成
frame_1 = Frame(root, bg='green', width=500, height=200)
frame_2 = Frame(root, bg='pink', width=500, height=300)
frame_1.pack(padx=10, pady=10)
frame_2.pack(padx=10, pady=(0, 10))
frame_2.pack_propagate(0)

# エントリーの作成
entry_1 = Entry(frame_1, width=30) # 幅30のエントリーをframe_1に配置する設定
entry_1.grid(row=0, column=0, padx=5, pady=5) 
frame_1.grid_propagate(0)

button_1 = Button(frame_1, text='出力', command=print_text)
button_1.grid(row=0, column=1, padx=5, pady=5, ipadx=30)

# 引数を渡して関数を実行
value = 0
button_2 = Button(frame_1, text='カウント', command=lambda:count(value))
button_2.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky='WE')

# ウィンドウのループ処理
root.mainloop()
