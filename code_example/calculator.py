from tkinter import *
from tkinter import RIGHT, END, DISABLED
from tkinter.constants import NORMAL
from decimal import Decimal
from tkmacosx import *


# ウィンドウの作成
root = Tk()
root.title('電卓アプリ')
root.iconbitmap('calculator.ico')
root.geometry('680x260')
root.resizable(0, 0)


# 関数の定義
def clear_number():
    screen.delete(0, END)

    unlock_button()


def negate():
    calculated_number = -1 * Decimal(screen.get())
    # 結果を表示するために現在のスクリーンに表示されている数字を削除
    screen.delete(0, END)
    screen.insert(0, calculated_number)


def percentage():
    calculated_number = 0.01 * Decimal(screen.get())
    # 結果を表示するために現在のスクリーンに表示されている数字を削除
    screen.delete(0, END)
    screen.insert(0, calculated_number)


def add_element(number):
    screen.insert(END, number)

    # .が挿入された場合、それ以降、.を挿入できなくする処理
    if '.' in screen.get():
        decimal_button.config(state=DISABLED)


def unlock_button():
    decimal_button.config(state=NORMAL)
    add_button.config(state=NORMAL)
    substract_button.config(state=NORMAL)
    multiply_button.config(state=NORMAL)
    divide_button.config(state=NORMAL)


def operate(operator):
    global operation, first_number
    # 演算の種類と入力された数字の保持
    operation = operator
    first_number = screen.get()

    # 最初の数字を削除
    screen.delete(0, END)

    # =またはclearが押されるまで演算ボタンを押せなくする処理
    add_button.config(state=DISABLED)
    substract_button.config(state=DISABLED)
    multiply_button.config(state=DISABLED)
    divide_button.config(state=DISABLED)

    decimal_button.config(state=NORMAL)


def calculate():
    # 演算の実行
    if operation == 'add':
        calculated_number = Decimal(first_number) + Decimal(screen.get())
    elif operation == 'substract':
        calculated_number = Decimal(first_number) - Decimal(screen.get())
    elif operation == 'multiply':
        calculated_number = Decimal(first_number) * Decimal(screen.get())
    elif operation == 'divide':
        if screen.get() == '0':
            calculated_number = 'ERROR'
        else:
            calculated_number = Decimal(first_number) / Decimal(screen.get())

    # 計算結果を表示するために現在スクリーンに表示されている数字を削除
    screen.delete(0, END)
    screen.insert(0, calculated_number)

    # ボタンのロック解除
    unlock_button()


# 色とフォントの設定
screen_font = ('Segoe UI', 30, 'bold')
button_font = ('Segoe UI', 20, 'bold')
light_orange = '#FFEFD5'
light_gray = '#DCDCDC'
orange = '#FFA500'


# フレームの作成
screen_frame = LabelFrame(root)
button_frame = LabelFrame(root)
screen_frame.pack(padx=2, pady=(5, 0))
button_frame.pack(padx=2)


# エントリーの作成
screen = Entry(screen_frame, width=40, font=screen_font, bg=light_orange, justify=RIGHT, borderwidth=5)
screen.pack()


# ボタンの作成
clear_button = Button(button_frame, text="C", font=button_font, bg=light_gray, command=clear_number)
negate_button = Button(button_frame, text="+/-", font=button_font, bg=light_gray, command=negate)
percentage_button = Button(button_frame, text="%", font=button_font, bg=light_gray, command=percentage)
divide_button = Button(button_frame, text="÷", font=button_font, bg=orange, command=lambda: operate('divide'))
seven_button = Button(button_frame, text="7", font=button_font, bg='black', fg='white', command=lambda: add_element(7))
eight_button = Button(button_frame, text="8", font=button_font, bg='black', fg='white', command=lambda: add_element(8))
nine_button = Button(button_frame, text="9", font=button_font, bg='black', fg='white', command=lambda: add_element(9))
multiply_button = Button(button_frame, text="x", font=button_font, bg=orange, command=lambda: operate('multiply'))
four_button = Button(button_frame, text="4", font=button_font, bg='black', fg='white', command=lambda: add_element(4))
five_button = Button(button_frame, text="5", font=button_font, bg='black', fg='white', command=lambda: add_element(5))
six_button = Button(button_frame, text="6", font=button_font, bg='black', fg='white', command=lambda: add_element(6))
substract_button = Button(button_frame, text="-", font=button_font, bg=orange, command=lambda: operate('substract'))
one_button = Button(button_frame, text="1", font=button_font, bg='black', fg='white', command=lambda: add_element(1))
two_button = Button(button_frame, text="2", font=button_font, bg='black', fg='white', command=lambda: add_element(2))
three_button = Button(button_frame, text="3", font=button_font, bg='black', fg='white', command=lambda: add_element(3))
add_button = Button(button_frame, text="+", font=button_font, bg=orange, command=lambda: operate('add'))
zero_button = Button(button_frame, text="0", font=button_font, bg='black', fg='white', command=lambda: add_element(0))
decimal_button = Button(button_frame, text=".", font=button_font, bg='black', fg='white', command=lambda: add_element('.'))
equal_button = Button(button_frame, text="=", font=button_font, bg=orange, command=calculate)


# 1行目の配置
clear_button.grid(row=0, column=0, sticky='WE', pady=1)
negate_button.grid(row=0, column=1, sticky='WE', pady=1)
percentage_button.grid(row=0, column=2, sticky='WE', pady=1)
divide_button.grid(row=0, column=3, sticky='WE', pady=1)


# 2行目の配置
seven_button.grid(row=1, column=0, sticky='WE', ipadx=20, pady=1)
eight_button.grid(row=1, column=1, sticky='WE', ipadx=20, pady=1)
nine_button.grid(row=1, column=2, sticky='WE', ipadx=20, pady=1)
multiply_button.grid(row=1, column=3, sticky='WE', ipadx=20, pady=1)


# 3行目の配置
four_button.grid(row=2, column=0, sticky='WE', pady=1)
five_button.grid(row=2, column=1, sticky='WE', pady=1)
six_button.grid(row=2, column=2, sticky='WE', pady=1)
substract_button.grid(row=2, column=3, sticky='WE', pady=1)


# 4行目の配置
one_button.grid(row=3, column=0, sticky='WE', pady=1)
two_button.grid(row=3, column=1, sticky='WE', pady=1)
three_button.grid(row=3, column=2, sticky='WE', pady=1)
add_button.grid(row=3, column=3, sticky='WE', pady=1)


# 5行目の配置
zero_button.grid(row=4, column=0, sticky='WE', columnspan=2, pady=1)
decimal_button.grid(row=4, column=2, sticky='WE', pady=1)
equal_button.grid(row=4, column=3, sticky='WE', pady=1)


# ウィンドウのループ処理
root.mainloop()
