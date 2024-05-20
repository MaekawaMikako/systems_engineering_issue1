from tkinter import *
from tkmacosx import *

def print_number():
    if number.get() == 1:
        label_number = Label(frame_2, text='1が選択されました')
    elif number.get() == 2:
        label_number = Label(frame_2, text='2が選択されました')

    label_number.pack()


# ウィンドウの作成
root = Tk()
root.title('Radio button practice!')
root.iconbitmap('icon.ico')
root.geometry('550x550')
root.resizable(0, 0)


# フレームの作成
frame_1 = LabelFrame(root, text='テキストフレームです')
frame_2 = Frame(root)
frame_1.pack(padx=10, pady=10)
frame_2.pack(padx=10, pady=(0, 10))


# 整数の保持用にインスタンスを作成
number = IntVar()
number.set(1)


# ラジオボタンの作成
radio_1 = Radiobutton(frame_1, text='1を出力します', variable=number, value=1)
radio_2 = Radiobutton(frame_1, text='2を出力します', variable=number, value=2)
radio_1.grid(row=0, column=0, padx=10, pady=10)
radio_2.grid(row=0, column=1, padx=10, pady=10)

button_1 = Button(frame_1, text='出力', command=print_number)
button_1.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# ループ処理
root.mainloop()
