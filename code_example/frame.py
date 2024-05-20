from tkinter import *
from tkmacosx import SFrame

# ウィンドウの作成
root = Tk()
root.title('Frame practice')
root.iconbitmap('icon.ico')
root.geometry('550x550')
root.resizable(0, 0)

# なぜframeを使うのか？
# tkinter.Label(root, text='test').pack()
# tkinter.Button(root, text='test').grid(row=0, column=0)
# 上のコードはエラーが出ます。メインウィンドウにpackとgridを混在させることができません。

# frameの作成
#frame_1 = Frame(root, bg='yellow') # for windows OS
frame_1 = SFrame(root, bg='yellow') # for mac OS
#frame_2 = Frame(root, bg='green')
frame_2 = SFrame(root, bg='green') # for mac OS
frame_3 = LabelFrame(root, text='ラベルフレームです', borderwidth=5)

# frameをroot上に配置
frame_1.pack(fill='both', expand=True)
frame_2.pack(fill='both', expand=True)
frame_3.pack(fill='both', expand=True)

# ウィジェットの配置
Label(frame_1, text='テスト').pack()
Label(frame_1, text='テスト').pack()
Label(frame_1, text='テスト').pack()

Label(frame_2, text='テスト').grid(row=0, column=0)
Label(frame_2, text='テスト').grid(row=1, column=1)
Label(frame_2, text='テスト').grid(row=2, column=2)
# tkinter.Label(frame_2, text='ggggggggggggggggggggggggggggggggggggg').grid(row=3, column=0)

Label(frame_3, text='ggggggggggggggggggggggggggggggggggggg').grid(row=0, column=0)


# ウィンドウのループ処理
root.mainloop()
