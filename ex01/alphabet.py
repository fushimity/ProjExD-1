#消えたアルファベットを探すゲーム

from random import sample as sp
import time

num_of_alphabet = 26        #全アルファベット総数
num_of_all_chars = 10       #対象文字数
num_of_abc_chars = 2        #欠損文字数
num_of_trials = 2           #挑戦回数

def shutudai(alphabet):
    #全アルファベットから10個分検索をかける
    all_chars = sp(alphabet, num_of_all_chars)
    print("対象文字 : ")
    for c in all_chars :
        print(c, end=" ")
    print()

    # 対象文字から欠損文字を2個選択する.(重複しないように)
    abc_chars = sp(all_chars, num_of_abc_chars)
    print("欠損文字(デバッグ用) : ")

    for c in abc_chars : 
        print(c, end=" ")
    print()

    print("表示文字 : ")
    for c in all_chars:
        #abc_charsに含まれていなければ表示文字
        if c not in abc_chars :
            print(c, end = "")
    print()

    return abc_chars


def kaitou(abc_chars):
    num = input("欠損文字はいくつあるでしょうか? : ")
    if num != num_of_abc_chars:
        print("不正解です.")
    
    else :
        print("正解です. それでは, 具体的に欠損文字を1つずつ入力して下さい.")
        
        for i in range(num) :            
            ans = input(f"{i + 1}つ目の文字を入力して下さい : ")

            if ans not in abc_chars : 
                print("不正解です.")
                return False
            else :
                abc_chars.remove(ans)   # 正解した欠損文字を削除する. 

        print("全部正解です. ")
        return True


if __name__ == "__main__":
    st = time.time()
    
    alphabet = [chr(i + 65) for i in range(num_of_alphabet)]    # alphabetをリスト化して入れてあげる.
    print(alphabet)
    for i in range(num_of_trials):
        abc_chars = shutudai(alphabet)
        ret =  kaitou(abc_chars)
        if ret :
            break
        else :
            print("-" * num_of_all_chars)

    ed = time.time()

    print(f"所要時間：{(ed-st):.2f}秒")