# 列表list、列表的用法
# 列表可以存放很多值得資料型態

# 如果有5位的話，這樣寫就很麻煩，故可以改用列表的方式
#方法1，慢慢列出每項
score1 = 90
score2 = 70
score3 = 50 
score4 = 60
score5 = 30

#方法2，利用列表方式，利用中括號[] 
scores = [90,70,50,60,30]
friends = ["小黑","小黃","小綠"] 
things = [90,"小黑",True]
print(scores)
print(friends)
print(things)
print(scores[0])   #找出scores裡面第一個數字是哪一個
print(scores[-1])  #找出scores裡面最後數字的是哪一個
print(scores[0:2]) #找出scores裡面第一位到第二位數字之前的是哪一個，即是90,70
print(scores[1:])  #找出scores裡面70後面的數字
print(scores[:4])  #找出scores裡面80前面的數字(不包含30)

#將scores中的90改為20分
scores[0] = 20  #將scores中的90改為20分
print(scores)

# 列表常用的函數
# 1.延伸: .extend() ，()括號裡面要加入列表
scores.extend(friends)  #scores列表後面加上friends列表
print(scores)


# 2.列表後面加上一個值  .append()
scores.append(25)  #列表後面加上一個值
print(scores)


# 3.列表中的某一位插入一個值  .insert()
scores.insert(2,15)  #列表中第2位插入15
print(scores)


# 4.刪除列表中的值  .remove()
scores.remove(70)  #刪除列表中70的值
print(scores)


# 5.清空列表表中全部的值  .clear()
# scores.clear()  #清空列表表中全部的值 
# print(scores)


scores = [90,70,50,60,30]  #因為上面被清空了，所以在重設一個列表
# 6.刪除列表中的最後一位的值  .pop()
scores.pop()  #刪除列表中的最後一位的值
print(scores)


# 7.將列表由小到大排列  .sort()
scores = [90,70,50,60,30] 
scores.sort()  #將列表由小到大排列
print(scores)


# 8.將列表做反轉  .reverse()
scores = [90,70,50,60,30] 
scores.reverse()  #將列表做反轉
print(scores)

# 9.將列表做反轉  .reverse()
scores = [90,70,50,60,30] 
scores.reverse()  #將列表做反轉
print(scores)

# 10.找出列表中的數字在第幾位 .index()
scores = [90,70,50,60,30] 
print(scores.index(90))  #找出列表中的數字在第幾位 


# 11.找出列表中的搜尋的數字有幾個 .count()
scores = [90,90,50,90,30] 
print(scores.count(90))  #找出列表中90數字有幾個 


# 12.列表的長度: len(scores)
scores = [90,90,50,90,30] 
print(len(scores)) #找出列表有幾個數字(列表的長度) 


print(scores.count(90))