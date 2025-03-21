# 函式 function

# 1.函數的名稱只能是英文or數字or _的組合
# 2.函數的開頭不可以是數字

#1.定義一個簡單函式，使這函示可以印出hello 
def hello():  # 先定義一個函式叫做Hello
    print("hello") #想要這個函示幫我做的動作是印出hello這個字串，故需要在函式的內部輸入(前面要留空白，留4個空白建或是tab)
# print("您好") #這行不是函式的內部，因為沒有留白
# 故 7~8行 就是定義一個hello的函示，hello函式的功能是印出hello
hello()  #呼叫函式hello()，即會印出hello，呼叫函式不需要留白


#2.使函式可以傳入參數的
def hello(name,age):
    print("hello" + name +"你今年" + age + "歲") 

hello("小白", "87") # 數字87需要用雙引號變為字串"87"，這樣才可以字串的連接 


#3.使函式可以傳入參數的法2 (如果age要用數字的話)
def hello(name,age):
    print("hello" + name +"你今年" + str(age) + "歲") # age需要加上str(age)變成字串後才可用字串的相加

hello("小白", 87)   #小白是字串，87是數字


#4.函式參數內的相加
def add(number1,number2):
    print(number1 + number2 ) 

add(88, 9) # 數字87需要用雙引號變為字串"87"，這樣才可以字串的連接 


#5.函式的回傳return !!!!!!!!!!!!!!!!!!!!
#法1
def add(number1,number2):
    # print(number1 + number2 ) #此行其實沒有用，因為被return給取代了
    return 10 #函式裡面有return，就會將我們要呼叫的值覆蓋掉

print(add(2,3)) #return會覆蓋掉呼叫這行，故return會將add(2,3)取代掉，所以才會印出10


#法2 沒有用return， 但她跟法3是一樣的意思
def add(number1,number2):
    print(number1 + number2 ) 

add(2,3)


#法3 使用retuen
def add(number1,number2):
    return number1+number2 #故這裡就是retuen(2+3)的意思，故return後面的值就是 = add(2,3)

print(add(2,3)) # 此行等於 print(5)
print((add(2,3))*8)  #用return的好處，可以對回傳的值再去最近一步的運算例如*8

# 但為什麼要用return呢，看起來明明比較麻煩 !!!!!!!!!!!!!!!!!
# 因為我們常常不單只要呼叫完函示就沒事了，可能還會對它回傳的值去做計算。 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# 考題一: 想一下會run出什麼東西 ~~~
def add(num1,num2):
    print(num1+num2)   #印出3+4=7
    return 10          #回傳值為10

value = add(3,4)  # 可以用變數的概念去相等於我們要呼叫的函數
print(value)


# 練習 
def add(num4,num5):
    print(num4+num5)
    return num4+num5

value = add (45,46)
print (value*5)



# 考題二: 想一下會run出什麼東西 ~~~
def add(num1,num2):
    print(num1+num2)
                        
value = add(3,4)  #如果沒有return,python會自動幫我們return none
print(value)


# 6.當函式在運行時，碰到return就會直接結束，不會執行函式下面的程式
def add(num1,num2):
    print(num1+num2)
    return 10
    print("你好") #這行不會被印出，因為函式碰到return就會直接結束

value = add(5,6)
print(value)