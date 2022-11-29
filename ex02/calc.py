import tkinter as tk
import tkinter.messagebox as tkm


#3. クリックした際の反応
def Button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo(txt, f"[{txt}]ボタンが押されました.")

# 1. ウィンドウの作成
root = tk.Tk()
root.title("calc_GUI")
root.geometry("300x500")

#4. ボタンの上に, テキスト入力欄を追加

entry = tk.Entry(root, justify="right", width = 10, font=("", 40))
entry.grid(row = 0, column = 0, columnspan = 3)

#2. ボタンの作成

r = 1   # 入力欄とボタンの位置を重複させないようにしてあげる.
c = 0

for num in range(9, -1, -1):
    button = tk.Button(root, text=num, width = 4, height = 2,
                       font = ("", 30))
    button.grid(row=r, column=c)

    c += 1

    if c % 3 == 0:
        r += 1
        c = 0

    #クリック時の処理
    button.bind("<1>", Button_click)

root.mainloop()