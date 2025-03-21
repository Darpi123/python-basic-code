# if判斷句 就是讓電腦在不同狀況下可以運行不同的程式

# 1. 如果判斷句
# 如果 我肚子餓
#   我就去吃飯   
hungry = True
if hungry:   #他會判斷hungry是否為True，如果是True的話就進去if判斷式
    print("我就去吃飯")

hungry = False
if hungry:   #他會判斷hungry是否為True，如果是False的話則不會進行if判斷式
    print("我就去吃飯")


#2. 如果，否則判斷句
#如果 今天下雨
#   我就開車去上班
#否則 
#   我就走路去上班
rainy = True   
if rainy:   #判斷rainy是否為True，如果是True的話就進去if判斷式
    print("我就開車去上班")
else:       #如果rainy為False，則進入else裡
    print("我就走路去上班")



#3. 如果，或是如果。否則判斷句
#如果 你考100分
#   我給你1000元
#或是如果 你考80分以上
#   我給你500元
#或是如果 你考60分以上
#   我給你100元
#否則
#   你給我300元
score = 59
if score == 100: # ==的意思為判斷左右是否相等，如果相等即為 (score == 100) 就是True的意思
    print("我給你1000元")
elif score >= 80:  # >=的意思為判斷左邊是否大於等於右邊，如果符合即為 (score >= 100) 就是True的意思
    print("我給你500元")
elif score >= 60:
    print("我給你100元")
else:
    print("你給我300元")


#4. 如果，且 的判斷句
#如果 你考100分 且 今天下雨
#   我給你1000元
#否則
#   你給我105元
 
score = 100
rainy = True
if score ==100 and rainy: # and 的判斷式意思為 and左邊要是True 與 and右邊也要是True，才會往下進行
    print("我給你1000元")
else:
    print("你給我105元")


#5. 如果，或 的判斷句
#如果 你考100分 或 今天下雨
#   我給你1000元
#否則
#   你給我107元
score = 100
rainy = True
if score == 100 or rainy:  # or 的判斷式意思為 or左邊要是True 或是 or右邊是True，其中一個為符合，就會往下進行
    print("我給你1000元")
else:
    print("你給我107元")

#6. 如果，或，沒有 的判斷句
#如果 你考100分 或 沒有下雨
#   我給你1000元
#否則
#   你給我109元
score = 90
rainy = True #True為有下雨
if score == 100 or not(rainy): 
    print("我給你1000元")
else:
    print("你給我109元")


#7. 如果，沒有，或，沒有 的判斷句
#如果 你沒有考100分 或 沒有下雨
#   我給你1000元
#否則
#   你給我109元
score = 90
rainy = True #True為有下雨
if score!=100 or not(rainy):  #如果score不等於100即(score!=100)為True
    print("我給你1000元")
else:
    print("你給我111元")


# 練習題: 假設有一個函式為max_num ，當傳入三個值的時候，他會回傳這三個數字哪一個數字最大
# 法一(不用return)
def max_num(num1,num2,num3):
    print(max(num1,num2,num3))

max_num(3,5,9)

# 法二(用return)
def max_num(num1,num2,num3):
    return max(num1,num2,num3)

print(max_num(3,5,9))


# 法三(用return 和 if判斷式)
def max_num(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:   #也可以這樣寫 elif num3>=num1 and num3>=num2:
        return num3
    
print(max_num(3,5,9))
    



# 與上面的練習題一樣，只是在寫一次
# 練習題: 假設有一個函式為max_num ，當傳入三個值的時候，他會回傳這三個數字哪一個數字最大
#1. 不用if
def max_num(num4,num5,num6):
    return max(num4,num5,num6)

print(max_num(4,5,6))

# 2 不用retuen
def max_num(num4,num5,num6):
    print(max(num4,num5,num6))

max_num(4,5,6)

#3. 用if判斷句
def max_num(num4,num5,num6):
    if num4>num5 and num4>num6:
        print(num4)
    elif num5>num4 and num5>num6:
        print(num5)
    else:
        print(num6)
max_num(3,400,5)

#4.用if判斷句然後回傳
def max_num(num4,num5,num6):
    if num4>num5 and num4>num6:
        return num4
    elif num5>num4 and num5>num6:
        return num5
    else:
        return num6
print(max_num(3154163,400,5))