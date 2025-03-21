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

from question import Question   #從question模組裡面只引入Question類別
test = [
    "1+3=?\n(a) 2\n(b) 3\n(c) 4\n\n",
    "1公尺等於多少公分?\n(a) 10\n(b) 100\n(c) 1000\n\n",
    "香蕉是什麼顏色?\n(a) 黑色\n(b) 黃色\n(c) 白色\n\n" 
]
# print(test[0])   #這個可以參考16.2D.py那邊


# 使用新的資料型態(Question)來表達我們的問題，並把它放在questions裡面
questions = [
    Question(test[0],"c"),  # 參數1為問題的描述，參數2為答案
    Question(test[1],"b"),  # 參數1為問題的描述，參數2為答案
    Question(test[2],"b")   # 數1為問題的描述，參數2為答案
]




# 小小延伸1
# print(questions.description) #這樣會錯誤，因為questions是一個列表，裡面存放的是Question類別的物件，但列表qs本身沒有description的屬性，只有Question才有
# print(qs[0].description) 這樣才對

# 小小延伸2
# print(Question.description) 這樣也會錯誤，Question 是一個類別（class），但 description 是它的物件屬性。你必須先創建 Question 物件，才能存取 description。
# 這樣才對
# q1 = Question(test[0],"c")
# print(q1.description)



# 定義一個函式來跑測驗
def run_test(questions):  # 定義一個run_test函式來跑測驗，函示裡要傳入一個列表(questions)
    score = 0   #分數
    for question in questions:  #建立for迴圈，有幾題就要跑幾次
        answer = input(question.description + "答案為?")    #答案會等於我們輸入的答案，input題示為題目，且因為questions的第一行已經跑進去question了，所以如果要讀取題目，需要打question.description
        if answer == question.answer:   # 答案是否正確
            score +=1   #分數就加1
    print("你得到"+ str(score)+ "分，共" + str(len(questions))+"題" )

run_test(questions)


