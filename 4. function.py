# 常見的函式 function

phrase = "Hello Mr.White"
print(phrase)  

#1.字串變全小寫
phrase = "Hello Mr.White"
print(phrase.lower())  #變小寫

#2.字串變全大寫
phrase = "Hello Mr.White"
print(phrase.upper())  #變大寫


#3.判斷字串是否全都大寫
phrase = "Hello Mr.White"
print(phrase.isupper())  #判斷字串是否全都大寫

#4.判斷字串是否全都小寫
phrase = "Hello Mr.White"
print(phrase.islower())  #判斷字串是否全都小寫


#5.函式的疊加
phrase = "Hello Mr.White"
print(phrase.lower().islower())  #變小寫後判斷字串是否全都小寫

#6.[] 中括號的用法(字串的位置)
phrase = "Hello Mr.White"
        # 0123456789    位置
print(phrase[6])   #中括號裡面的數字為字串的位置,且起始位置為0
print(phrase[0:3]) #位置0~位置3之前都印出


#7. 想要找字串裡的位置是多少
phrase = "Hello Mr.White"
        # 0123456789    位置
print(phrase.index("H"))  #找出字串中H的位置是多少
print(phrase .index("e")) #找出字串中e的位置是多少

#8. replace 函示
phrase = "Hello Mr.White"
        # 0123456789    位置
print(phrase.replace("H","h"))  #將某個文字替換成別的文字 (將大寫的H替換成小寫的h)
print(phrase .replace("l","L"))

