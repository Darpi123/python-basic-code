#模組module的使用
#模組就是python的一個檔案，這個檔案可以給我們其他python程式做引入，引入之後就可以使用這個模組裡面的變數或是函式



# 1. 如何引入自己寫的module :
import tool  #將tool.py整個module引入進來這裡，所以會將tool裡面的函數的答案3傳來這裡

#要如何使用module裡面的變數或是函數
print(tool.name)    #引入module裡面的變數
print(tool.age)     #引入module裡面的變數
print(tool.max_num(7,8,9))  #引入module裡面的函數




# 2. 引入Python內建的module :
# 上網搜尋 :Python module list 
import token 
token.AT  #隨便選的

#3.如果想找到內建module的位置在哪: 使用sys
import sys
print(sys.path)
# 下方terminal結尾式Lib就是Python存放內建Module的路徑 C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python312\\Lib'


#4.使用第三方的Module，要下載，使用pip來下載，去Terminal下方打pip install numpy
#  這裡我有用虛擬環境下載numpy 
import numpy 
numpy.acos #隨便選的


#5.如果覺得第三方module名字太長，可以改名子，ex:將numpy改成np
import numpy as np  #將numpy改成np
np.acos



#6.如何引入模組裡面的一個小類別 ? !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
from tool import tool1
print(tool1)
