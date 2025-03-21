#檔案讀取、寫入

# open("檔案路徑", mode="開啟模式")
# 絕對路徑ex:   D:/desk/Python/python/white/123.txt ，記得斜線要相反!!!!!!!!!!!!!!!!!!!!!!!!!!
# 相對路徑   是以程式檔案(17.file.py)的位置做延伸 ex:假如路徑只打這樣123.txt， 但是其實他前面簡略D:/desk/Python/python/white

# 開啟模式="r" 讀取
# 開啟模式="w" 覆寫
# 開啟模式="a" 在原先的資料後加東西

#原始123.txt的內容是 :
# 78
# 79
# 80
# 81
# 82 


# 1. 開啟123.txt檔案並讀取
#法1 : 使用絕對路徑
file = open("D:/desk/Python/python/white/123.txt", mode="r")
print(file.read())  #讀取檔案，讀取完後將檔案裡面的內容印出來
file.close()    #讀取完檔案後，把檔案關起來，財不會佔用電腦資源

#法2 : 使用相對路徑
file = open("123.txt", mode="r")
print(file.read())
file.close()    #讀取完檔案後，把檔案關起來，財不會佔用電腦資源


# 2. 開啟檔案開啟檔案並只讀第一行，使用readline
file = open("123.txt", mode="r")
print(file.readline())     #只讀第一行
file.close()    #讀取完檔案後，把檔案關起來，財不會佔用電腦資源


# 3 開啟檔案開啟檔案並只讀第一、二行(或是多行)，使用readline
#法1 : 使用兩次readline
file = open("123.txt", mode="r")
print(file.readline())     #只讀第一行
print(file.readline())     #再讀第二行
file.close()    #讀取完檔案後，把檔案關起來，財不會佔用電腦資源

#法2 : 用for迴圈，一次讀很多行
file = open("123.txt", mode="r")
for content in file:
    print(content)
file.close()    #讀取完檔案後，把檔案關起來，財不會佔用電腦資源


#4. readlines 將每一行的資料，放到一個列表裡面 ，結果有跑出\n是因為有換行
file = open("123.txt", mode="r")
print(file.readlines())     
file.close()    #讀取完檔案後，把檔案關起來，財不會佔用電腦資源



#5. 開啟檔案後，覆寫
file = open("123.txt", mode="w")
file.write("hello")
file.close()  



#6-1 開啟檔案後，在原先的資料再寫東西
file = open("123.txt", mode="a")
file.write(" \n您好")   #會什麼去VS code裡的123.txt會顯示亂碼，因為123.txt他的編碼方式並不支援中文，所以才會顯示亂碼
file.close() 


#6-2. 開啟檔案後，在原先的資料再寫東西，解決 #6-1 打中文會有亂碼的問題
file = open("123.txt", mode="a", encoding= "utf-8" )    #改善亂碼問題，故添加第三個參數(編碼的方式)，ex:  utf-8支援中文
file.write(" \n您好")   #會什麼去VS code裡的123.txt會顯示亂碼，因為123.txt他的編碼方式並不支援中文，所以才會顯示亂碼
file.close() 



# 推薦的寫法 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#7. 不用每次都關閉的方法，故不須要打file.close 
with open("123.txt", mode="a", encoding= "utf-8" ) as file:   #這行跟line72行的意思一樣，但使用with as的話 會自動關閉檔案
    file.write(" \n哈哈") 

# with open("123.txt" , mode="r") as file:
#     print(file.read())