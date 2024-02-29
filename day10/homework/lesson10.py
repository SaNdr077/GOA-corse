#1) დაწერეთ პროგრამა, რომელშიც შექმნით ჩვენი ჯგუფელებისგან სიას.
# რენდომად გამოიძახებთ ერთ ჯგუფელს, თუ კითხვაზე უპასუხებს
# მოემატება 1 ქულა და გადავალთ შემდეგზე(ოღონდ ეს ვეღარ უპასუხებს იმ დღეს)
# ( ანუ remove დაგჭირდებათ),
from turtle import *
import random

arr_of_students = ["giorgi", "giga", "nika", "temuri", "sandro", "luka"]
score = [10, -5]

while len(arr_of_students) > 0:
    students = random.choice(arr_of_students)
    print(students)
    answer = input ("you are studying goa: ")
    if answer == "yes":
        print (students, "added to you", score[0], "score")
        arr_of_students.remove(students)
    elif answer == "no":
        print (students, "added to you", score[1], "score")


#2) შექმენით random password generator პროგრამა რომელშიც დაგენერირდბა პაროლი,
# 8 სიმბოლოიანი, სადაც აუცილებლად 2 სიმბოლო იქნება !##%(#)^#,
# 2 სიმბოლო იქნება აბგქწეკჯასკჯქწე , 4 სიმბოლო იქნება ციფრები 215346347347
# მაგ: !n8391k*

my_arr = []
number = "123456789"
symbol = "!##%#^#"
chars = "qwertyuiopasdfghjklzxcvbnm"
password = ""
password_random = ""
for i in range(4):
    my_arr += random.choice(number)
for i in range(2):
    my_arr += random.choice(symbol)
    my_arr += random.choice(chars)
for i in range(len(my_arr)):
    current_char = random.choice(my_arr)
    password += current_char
    my_arr.remove(current_char)
print(password)

#3) turtle-თი რენდომ რიცხვებით დახაზეთ შედევრი 
# forward(random.randint(100))

speed(300)
colors = ["red", "blue", "green"]
for i in range(20000):
    color(random.choice(colors))
    forward(random.randint(0, 100))
    left(random.randint(0, 100))
exitonclick()
