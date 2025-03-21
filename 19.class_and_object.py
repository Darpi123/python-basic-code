# 類別class、物件object 
# 為什麼要用class和object，因為之前介紹的資料型態ex:數字、字串、布林值或是延伸的列表、元組和字典，但其實值這些還是沒有辦法表達現實生活中的很多東西，例如要如何表達人類，沒辦法用這些表達

# 故可以利用class去定義自己需要的資料型態

# 1.如要訂義一個手機
class Phone:    #使用class來去定義，Phone為我們要訂義的名字。 class只是一個模板，當我們創建手機時我們需要什麼資訊
    def __init__(self,os,number,is_waterproof): #需打__int__這個函數,Python才會知道這是初始的函數，(os, number, is_waterproof)這三個為我們定義的資料型態所需要的資訊 ,os為作業系統 , number為手機型號, is_waterproof為是否防水，然後self 為object本身
        self.os = os    #這個object本身有一個屬性叫做self.os，然後它的值等於我們傳入os的值， 
        self.number = number    #這個object本身有一個屬性叫做self.number，然後它的值等於我們傳入number的值
        self.is_waterproof = is_waterproof  #這個object本身有一個屬性叫做self.is_waterproof，然後它的值等於我們傳入is_waterproof的值

Phone1 = Phone("ios",123,True) #故os為ios , number為123，is_waterproof為True ，且這個Phone為object，再將phone裡面的資料傳進去Phone1裡

print(Phone1.os)    #如何取得物件裡面的屬性，利用Phone1.XX ，會得到ios
print(Phone1.number)    #如何取得物件裡面的屬性，利用Phone1.XX ，會得到123




#如有另外一台手機
Phone2 = Phone("andriod",456,False)
print(Phone2.os)    #如何取得物件裡面的屬性，利用Phone2.XX 

