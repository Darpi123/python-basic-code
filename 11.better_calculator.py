# 建立一個計算機

num1= float(input("請輸入第一個數 ")) #因為inputc會將所有我們的輸入預設為字串來看，所以添加float將字串轉為有小數的數字
op = input("請輸入運算符號 ")
num2= float(input("請輸入第二個數 "))

if op=="+":
    print(num1+num2)
elif op=="-":
    print(num1-num2)
elif op=="*":
    print(num1*num2)
elif op=="/":
    print(num1/num2)
else:
    print("不支援的運算")




#下面只是在練習一次

# num1= float(input("請輸入第一個數"))
# operation = input("請輸入運算符號")
# num2= float(input("請輸入第二個數"))

# if operation == "+":
#     print(num1+num2)
# elif operation== "-":
#     print(num1-num2)
# elif operation== "*":
#     print(num1*num2)
# elif operation=="/":
#     print(num1/num2)
# else:
#     print("error")