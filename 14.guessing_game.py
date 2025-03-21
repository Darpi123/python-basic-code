# 猜數字遊戲

# 遊戲一: 可以輸入無限次，判斷我們數字是否大於這個謎底，如果大於謎底的話會提示我們要小一點，如果數字於謎底的話，會提示我們大一點，直到我們猜對為止，如猜對謎底，遊戲會印出恭喜你贏了
secret_num = 77 #迷底
guess = None #guess這個變數是用來存放用戶輸入的猜測

while  secret_num != guess:
    guess = float(input("請輸入一個數字 "))
    if guess < secret_num:
        print("再大一點")
    elif guess > secret_num:
        print("再小一點")
 
print("恭喜贏了")



# 遊戲二: 只能輸入三次，判斷我們數字是否大於這個謎底，如果大於謎底的話會提示我們要小一點，如果數字於謎底的話，會提示我們大一點，如猜對謎底，遊戲會印出恭喜你贏了
# 法一(我自己寫的方法)
secret_num = 78
guess = None
i = 0 #猜的次數
while  secret_num != guess and i<3:
    i +=1  # 也可以寫成 i=i+1
    guess = float(input("請輸入一個數字 "))
    if guess < secret_num:
        print("再大一點")
    elif guess > secret_num:
        print("再小一點")
 
if secret_num != guess and i>=3:
    print("輸入超過三次，你輸了")
else:
    print("恭喜贏了")


# 法二(小白寫的方法)
secret_num = 79
guess = None
guess_count = 0 #猜的次數
guess_limit =3  #最多只能猜三次
out_of_limit = False #是否有猜超過三次，一開始沒有超過三次故為False

while  secret_num != guess and not(out_of_limit):  #數字跟謎底要不同且沒有超過三次的話，才會進入迴圈
    guess_count +=1  # 也可以寫成 guess_count=guess_count+1
    if guess_count <= guess_limit:
        guess = float(input("請輸入一個數字 "))
        if guess < secret_num:
            print("再大一點")
        elif guess > secret_num:
            print("再小一點")
    else:
        out_of_limit = True #因為次數超過三次，故改為True

if out_of_limit:  # 也可以寫成 out_of_limit ==True:
    print("輸入超過三次，你輸了")
else:
    print("恭喜贏了")








# 下面是再寫一遍的

# 遊戲一: 可以輸入無限次，判斷我們數字是否大於這個謎底，如果大於謎底的話會提示我們要小一點，如果數字於謎底的話，會提示我們大一點，直到我們猜對為止，如猜對謎底，遊戲會印出恭喜你贏了
secret_num = 78 
num = None

while num != secret_num:
    num = float(input("請猜數字: "))
    if num>secret_num:
        print("數字太大了")
    elif num<secret_num:
        print("數字太小了")

print("恭喜你贏了")




# 遊戲二: 只能輸入三次，判斷我們數字是否大於這個謎底，如果大於謎底的話會提示我們要小一點，如果數字於謎底的話，會提示我們大一點，如猜對謎底，遊戲會印出恭喜你贏了
secret_num = 78 
num = None
time = 1

while num != secret_num and time<4:
    num = float(input("請猜數字: "))
    time += 1
    if num>secret_num:
        print("數字太大了")
    elif num<secret_num:
        print("數字太小了")

if num != secret_num and time>=4:
    print("你猜超過3次了")
else:
    print("恭喜你贏了")


# 遊戲二: 只能輸入三次，判斷我們數字是否大於這個謎底，如果大於謎底的話會提示我們要小一點，如果數字於謎底的話，會提示我們大一點，如猜對謎底，遊戲會印出恭喜你贏了
secret_num = 79
guess = None
guess_count = 0
guess_limit = 3
out_the_limit = True

while guess!=secret_num and guess_count<guess_limit:
    guess_count += 1 
    guess = float(input("請猜數字: "))
    if  guess>secret_num:
        print("數字太大了")
    elif guess<secret_num:
        print("數字太小了")

if guess_count > guess_limit:
    print("猜超過3次了")
elif guess_count == guess_limit and guess!=secret_num :
    print("猜超過3次了")
else:
    print("恭喜你贏了")





