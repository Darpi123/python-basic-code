# 同20.practice.py，但是在寫第二遍

# 問答程式
# 題目一 :
# 題目1+3=?
# (a) 2
# (b) 3
# (3) 4

# 題目二 :
# 1公尺等於多少公分?
# (a) 10
# (b) 100
# (c) 1000

# 題目三 :
# 香蕉是什麼顏色?
# (a) 黑色
# (b) 黃色
# (c) 白色



# 可以看出每個問題都有兩個資訊，第一個為問題描述本身，第二個為問題的答案，因為一個問題有兩個資訊，所以可以定義成一個新的資料型態
# 定義一個新的資料型態question




# from question import Question 

test = [ 
    "1+3=? \n(a)2 \n(b)3 \n(c)4\n" ,
    "1公尺等於多少公分? \n(a)10 \n(b)100 \n(c)1000\n",
    "香蕉是什麼顏色? \n(a)黑色 \n(b)黃色 \n(c)白色\n"
    ]

class Question: 
    def __init__(self,description,answer):  #資訊1:問題描述，資訊2:答案
        self.description = description
        self.answer = answer


qs = [ 
    Question(test[0],"c"),  # 參數1為問題的描述，參數2為答案
    Question(test[1],"b"),  # 參數1為問題的描述，參數2為答案
    Question(test[2],"b")   # 數1為問題的描述，參數2為答案
]




#做一個方程式
def run_test(qs):
    score = 0 
    for questiona in qs:
        answer = input(questiona.description +  "答案為?" )
        if answer == questiona.answer:
            score += 1
      

    print("恭喜你的到"+str(score)+"分" +"總共"+ str(len(qs))+"題")


run_test(qs)


