# 元組tuple
# 元組與列表的差別在於: 元組創建後就不能做新增、修改和刪除
# 元組是應用於資料創建時怕被修改到，故可以使用元組存放就不能被修改了

scores = (90,80,60,70,50) #元組要用小括號，列表使用中括號
print(scores[0]) #找出scores裡面第一個數字是哪一個
print(scores[0:2]) #找出scores裡面第一位到第二位數字之前的是哪一個，即是90,80

# 1.元組的長度: len(scores)
print(len(scores))


# 2. 想更改元組的內容(無法改)
scores[0]=70 #無法更改元組的內容
print(scores) 


