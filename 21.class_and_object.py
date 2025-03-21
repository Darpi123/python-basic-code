# 物件函式
# 在物件裡面宣告一個函示

class Phone():
    def __init__(self,os,number,is_waterproof):
        self.os = os 
        self.number = number 
        self.is_waterproof = is_waterproof 


    # 1.宣告一個函式，來去判斷這個手機是不是ios
    def is_ios(self):   #這裡的self就是跟上面的self是一樣的意思 
        if self.os == "ios":
            return True
        else:
            return False
        

    # 2. 宣告一個函式，讓手機有相加的功能
    def add(self,number1,number2):
        answer = number1 + number2 
        return answer


Phone1 = Phone("ios",123,True)  #有一個手機叫做Phone1


print(Phone1.is_ios()) #印出是否為ios

print(Phone1.add(5,6))  #印出相加的數字

