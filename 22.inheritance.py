# 繼承 inheritance 

# 需參考類別 person 和 student
from student import Student


student1 = Student("white",87,"小白國小")
student1.print_school()
student1.print_name()   #雖然sutden裡面看起來沒有print_name的函示，但因為繼承Person，所以其實有print_name