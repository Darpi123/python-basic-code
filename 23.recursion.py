# 遞迴

# 不是用遞迴寫的方法 
def findGCD(n1, n2):
    while n2 != 0:
        n1, n2 = n2, n1%n2
    return n1

findGCD(12, 6)


# 利用遞迴方式 : 
#1. 找最大公因數: 
def findGCD(n1, n2):
    return n1 if n2 == 0 else findGCD(n2, n1%n2)      #如果n2等於0，那答案就是n1 ， 否則的話，請再幫我算一次findGCD(n2, n1%n2)


print(findGCD(16, 6))




# n 階乘
# n! = 1 x 2 x ... x n 
def factorial(n):
    result = 1 
    for i in range(1,n+1):
        result = result * i
    return result

print(factorial(5))   


# 法2: 利用 recursion(遞迴)
# 0! = 1 
# 1! = 1 
# (n-1)! = (n-2)! * (n-1)
# n! = (n-1)! * n  , n >= 1
def factorial1(n):
    if n == 0  or n == 1:
        return 1 
    else:
        return n *factorial1(n-1)
    
print(factorial1(5))   
