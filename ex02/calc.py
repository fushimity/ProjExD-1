import tkinter as tk

# 1. ウィンドウの作成
root = tk.Tk()
root.title("calc_GUI")
root.geometry("300x500")

#2. ボタンの作成

r = 0
c = 0

for num in range(9, -1, -1):
    button = tk.Button(root, text=num, width = 4, height = 2,
                       font = ("", 30))
    button.grid(row=r, column=c)
    c += 1
    if c % 3 == 0:
        r += 1
        c = 0

root.mainloop()