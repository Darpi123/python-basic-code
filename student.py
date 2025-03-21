# # 定義學生的名字、年紀和學校
# # 可以看出來student和person的類別其實很像，重複的程式碼很多，所以可以用繼承的方式去寫，就不用打這麼多程式碼了

# # 1. 一般的寫法會這樣寫，但跟person的類別比較的話發現重複太多程式碼了
# class Studnet:
#     def __init__(self,name,age,school):  
#         self.name = name
#         self.age = age 
#         self.school = school 


#     def print_name(self):
#         print(self.name)

#     def print_age(self):
#         print(self.age)

#     def print_school(self):
#         print(self.school)

# # Person1 = Person("white",87)



# # 2. 利用繼承的方式來打
# from person import Person  #引入person模組裡面的一個Person小類別 
# class Student(Person):  #Student繼承person 就等於是 將person裡面的類別複製到這裡來，可以看#3  
#     def __init__(self,name,age,school):  
#         self.name = name
#         self.age = age 
#         self.school = school 


#     def print_name(self):
#         print(self.name)

#     def print_age(self):
#         print(self.age)

#     def print_school(self):
#         print(self.school)



# #3. Student繼承person的寫法(方便簡化可以寫成#2的方法)，，

# from person import Person  
# class Student(Person):  
#     #這是從person複製過來的
#     # def __init__(self,name,age):  
#     #     self.name = name
#     #     self.age = age 


#     # def print_name(self):
#     #     print(self.name)

#     # def print_age(self):
#     #     print(self.age)

#    #這是原先student的類別
#     def __init__(self,name,age,school):  
#         self.name = name
#         self.age = age 
#         self.school = school 


#     # def print_name(self):
#     #     print(self.name)

#     # def print_age(self):
#     #     print(self.age)

#     def print_school(self):
#         print(self.school)



#4. Student繼承person的寫法，將#3多餘的程式碼刪掉(最終長這樣)

from person import Person  
class Student(Person):  

    def __init__(self,name,age,school):  
        self.name = name
        self.age = age 
        self.school = school 


    def print_school(self):
        print(self.school)