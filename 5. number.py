# 如何使用數字、數字的用法
# 以下為各種函數符號
# 一. 除法(省略小數點): //
# 二. 取餘數:  % 
# 三. 數字變成字串: str() , 字串變成數字(整數): int() ,  字串變成數字(有小數點): float()
# 四. 次方 pow()
# 五. 絕對值 abs()
# 六. 次方 pow()
# 七. 最大值 max()
# 八. 最小值 min()
# 九. 四捨五入 round()
# 十. 無條件捨取 floor()
# 十一. 無條件進位 ceil()
# 十二. 開根號 sqrt()
from math import *   #(引入模組) #如果想要更多數學函式就需要這個程式碼ex: floor、ceil、sqrt

# 乘法和除法
print(8*5)
print(8/3)

# 1.整數除法(省略小數點): 指令為 //
print(8//5)

# 2.連續運算(先乘除後加減)
print(8+8*5)
print((8+8)*5)

# 3.變數用法
number = 8
print(number*5)
print(number%5)  # 取餘數

# 4.數字變成字串 str() 就可以用字串的相加
print("會印出數字"+ str(number))  #數字變成字串

# 4.1 字串變成數字方法 int()

# 5.數字和字串 不能相加
# print( 8+ str(number))  #數字和字串 不能相加


# 7.絕對值 abs()
number1 = -8
print(abs(number1))

# 8.次方 pow()
number2 = 2
print(pow(number2,4)) #number2 的4次方 

# 9.最大值 max()
print(max(2,3,88,100,35,52,11,1111,2))

# 10.四捨五入 round()
print(round(4.4))  #4.4 取四捨五入

print(floor(4.4))  #4.4 無條件捨去


