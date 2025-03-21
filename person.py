# 定義一個人的名字和年紀

class Person:
    def __init__(self,name,age):  
        self.name = name
        self.age = age 


    def print_name(self):
        print(self.name)

    def print_age(self):
        print(self.age)


Person1 = Person("white",87)
# Person1.print_name()
