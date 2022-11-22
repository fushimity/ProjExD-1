#クイズゲームの実装
from random import choice as ch
import datetime


def shutudai(qa_lst):
   qa = ch(qa_lst)
   print("問題 : " + qa["q"])

   return qa["a"]

def kaitou(ans_lst):
    ans = input("答えるんだ : ")

    if ans in ans_lst : 
        print("正解!!!")
    else :
        print("出直してこい!!!")

    return st


if __name__ == "__main__":
    st = datetime.datetime.now()
    qa_lst = [
        {"q" : "サザエの旦那の名前は?", "a" : ["マスオ", "ますお"]},
        {"q" : "カツオの妹の名前は?", "a" : ["ワカメ", "わかめ"]},
        {"q" : "タラオはカツオから見てどんな関係?", "a" : ["甥", "おい", "甥っ子", "おいっこ"]},
    ]

    ans_lst = shutudai(qa_lst)
    
    kaitou(ans_lst)
    
    ed = datetime.datetime.now()

    '''
    print(ed)
    print(st)
    '''
    
    print("所要時間 : " + str((ed - st).seconds))