# 迷路ゲームの実装

import tkinter as tk
import maze_maker as mm
import tkinter.messagebox as tkm
from random import randint as rd

check = 0   # ゲーム動作しているかどうか.

def count_up():
    global tmr, jid, check
    label["text"] = tmr
    tmr += 1
    if check == 1:
        jid = None
    else :
        jid = root.after(1000, count_up)

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_proc():
    global cx, cy, mx, my   # こうかとんの位置を表す & 床の位置
    global check             # タイマー

    mx_rd, my_rd, all_rd = rd(1, 15), rd(1, 15), rd(1, 15)

    if key == "Up": my -= 1
    if key == "Down": my += 1
    if key == "Left": mx -= 1
    if key == "Right": mx += 1

    if maze_lst[mx][my] == 1: # 移動先が壁だったら,
        if key == "Up": my += 1
        if key == "Down": my -= 1
        if key == "Left": mx += 1
        if key == "Right": mx -= 1

    cx, cy = mx*100+50, my*100+50   # 位置の計算
    canvas.coords("kokaton", cx, cy)
    # 成功パターン
    if mx == 13 and my == 7:
        tkm.showinfo("おめでとう!", "よくできましたね.")
        check = 1
    elif mx_rd == all_rd and my_rd ==  all_rd :
        tkm.showwarning("警告!", "残念.そこは落とし穴でした~")
        tkm.showinfo("message", "もう一度やり直してね!")
        mx, my = 1, 1
    else :
        root.after(100, main_proc)

def show():
    tkm.showinfo("情報", "準備はいいですか? (OKを押すとスタートします.)")
    count_up()

if __name__ == '__main__':
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(root, width = 1500, height = 900, bg = "black")
    canvas.pack()

     # 時間計測部分
    label = tk.Label(root, text="-", font=("", 80))
    label.pack()
    tmr = 0
    jid = None

    maze_lst = mm.make_maze(15, 9)
    # print(maze_lst)
    mm.show_maze(canvas, maze_lst)

    mx, my = 1, 1
    # 画像描画
    cx, cy = mx*100+50, my*100+50
    tori = tk.PhotoImage(file = "../fig/8.png")
    canvas.create_image(cx, cy,
                        image = tori, 
                        tag = "kokaton")
    
    key = ""
    
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    show()
    main_proc()
    # root.after(0, show)
    root.mainloop()
