from tkinter import *
from PIL import ImageTk, Image


def display_image():
    global image_by_pillow

    image_by_pillow = ImageTk.PhotoImage(Image.open('mountain.jpg'))
    label_by_pillow = Label(root, image=image_by_pillow)
    label_by_pillow.pack()


# ウィンドウの作成
root = Tk()
root.title('Image practice!')
root.iconbitmap('icon.ico')
root.geometry('550x550')
root.resizable(0, 0)

# 画像の配置
image_1 = PhotoImage(file='dice.png') # png形式しか使えません。
label_1 = Label(root, image=image_1)
label_1.pack()

button_1 = Button(root, image=image_1)
button_1.pack()


# jpgの利用（エラーが出る）
# image_2 = PhotoImage(file='mountain.jpg')
# label_2 = Label(root, image=image_2)
# label_2.pack()


# pillowによってjpgを読み込んで表示
# image_by_pillow = ImageTk.PhotoImage(Image.open('mountain.jpg'))
# label_by_pillow = Label(root, image=image_by_pillow)
# label_by_pillow.pack()

display_image()

# ウィンドウのループ処理
root.mainloop()
