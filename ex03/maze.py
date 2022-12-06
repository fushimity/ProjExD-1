# 迷路ゲームの実装

import tkinter as tk
import maze_maker as mm

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_proc():
    global cx, cy   # こうかとんの位置を表す
    if key == "Up": cy -= 20
    if key == "Down": cy += 20
    if key == "Left": cx -= 20
    if key == "Right": cx += 20
    canvas.coords("kokaton", cx, cy)
    root.after(100, main_proc)

if __name__ == '__main__':
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(root, width = 1500, height = 900, bg = "black")
    
    # 画像描画
    cx, cy = 300, 400
    tori = tk.PhotoImage(file = "../fig/8.png")
    canvas.create_image(cx, cy,
                        image = tori, 
                        tag = "kokaton")
    canvas.pack()

    maze_lst = mm.maze_maker(15, 9)
    # print(maze_lst)

    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    main_proc()
    root.mainloop()
