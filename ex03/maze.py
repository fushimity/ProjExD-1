# 迷路ゲームの実装

import tkinter as tk

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
    key = ""
    root.mainloop()
