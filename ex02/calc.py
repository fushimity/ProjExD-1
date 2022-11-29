import tkinter as tk
import tkinter.messagebox as tkm


#3. クリックした際の反応
def Button_click(event):
    btn = event.widget
    txt = btn["text"]
    
    #7. =のときの挙動

    if txt == "=" :
        siki = entry.get()          # 数式の文字列
        
        try : 
            res = eval(siki)        # 数式文字列の評価

        # プラスを2回行ってからイコールを押すなど, 入力にミスが有った時.
        except SyntaxError : 
            tkm.showwarning("警告", "入力ミスがあります. もう一度試してみて下さい.")
            entry.delete(0, tk.END) # 表示文字列の削除

        entry.delete(0, tk.END)     # 表示文字列の削除
        entry.insert(tk.END, res)   # 結果の挿入
    
    else : # = 以外
        # tkm.showinfo(txt, f"[{txt}]ボタンが押されました.")
        #6. ボタンをクリックした時の挙動を変更
        entry.insert(tk.END, txt)

#1. ウィンドウの作成
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

    # クリック時の処理
    button.bind("<1>", Button_click)

    c += 1

    if c % 3 == 0:
        r += 1
        c = 0

#5. 空いたところに+=ボタンを追加.

symbol = ["+", "="]

for ope in symbol:
    button = tk.Button(root, text=ope, width = 4, height = 2,
                       font = ("", 30))

    button.grid(row=r, column=c)
    button.bind("<1>", Button_click)

    c += 1

    if c % 3 == 0:
        r += 1
        c = 0
    
root.mainloop()