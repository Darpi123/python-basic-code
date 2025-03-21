# for 迴圈
# for 變數 in 字串or列表:     ==>  他會in後面的字串切成一個一個地字元，然後一一放入變數裡面，列表也同樣意思
# #   要重複執行的程式碼

# # 1. 字串
for letter in "小白你好":  #將小白你好切成每個字元放入變數中
    print(letter)

# #2.列表
for num in [0,1,2,3,4]:
    print(num)

# #3.利用range
for num1 in range(100):     #會將0~99放入變數中
    print(num1)


# #4.抓中間的數字  ex:2~6
for num2 in range(2,7):     #會將2~6放入變數中
    print(num2)


# 練習 如何做出次方 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 如果要做出2的6次方，利用for迴圈要怎麼用
# print(pow(2,6)) = 64
#法一
def power(base_num,pow_num):
    result = base_num
    for index in range(pow_num-1):  #總共會執行{pow_num-1}次數，
        result = result*base_num
    return result   #將result回傳
print(power(2,6))  # 印出這個function執行的結果


#法二
def power(base_num,pow_num):
    result = 1
    for index in range(pow_num):  #總共會執行{pow_num-1}次數，
        result = result*base_num
    return result   #將result回傳
print(power(2,6))  # 印出這個function執行的結果




# 練習 如何做出次方 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 如果要做出2的6次方，利用for迴圈要怎麼用
# print(pow(2,6)) = 64

