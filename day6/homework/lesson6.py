#1)მომხმარებლის ნიშნებისგან გამოანგარიშება საშუალო არითმეტიკული და თუ ცხრაზე მეტი იქნება:
#დაუპრინტეთ გილოცავ მატრიცელო შენ გადმოგეცა 300 ლარიანი ბანძი ტოსტერი რასაც შეალიე შენი ცხოვრების წლები
#თუ ეს იქნება 5ზე ნაკლები: დაუპრინტე გილოცავ გაექეცი მატრიცას
#თუ იქნება 5 იდან 9 მდე: დაუპრინტე YOU ARE MID
#თუ იქნება 10ზე მეტი ან 0ზე ნაკლები: დაუპრინტე there is something wrong with you

num1 = float (input ("enter number1: "))
num2 = float (input ("enter number2: "))
num3 = float (input ("enter number3: "))
arithmetic = (num1 + num2 + num3)/3
if arithmetic > 9 and arithmetic <= 10:
    print ("""გილოცავ მატრიცელო შენ გადმოგეცემა 300 ლარიანი ბანძი 
              ტოსტერი რისთვისაც შეალიე შენი ცხოვრებისწლები""")
elif  arithmetic < 5 and arithmetic > 0:
        print ("გილოცავ, გაექეცი მატრიცას")

elif arithmetic >= 5 and arithmetic < 9:
        print ("YOU ARE MID")

else: 
        print ("there is something wrong with you")

#2)მომხმარებელს შეეკითხეთ ხელფასი
# თუ 10000ზე მეტია, დაუპრინტეთ, გოა-ში სწავლობდი?
# თუ 1000----10000 -ია , დაუპრინტეთ you mid
# თუ 1000-ზე დაბალია, დაუპრინტეთ, შემოსულიყავი გოაში, მატრიცელო

salary = int (input ("what is your salary? "))

if salary > 10000:
    print ("გოა_ში სწავლობდი?")
elif salary > 1000 and salary <10000:
    print ("you mid")
else:
    print ("შემოსულიყავი გოაში მატრიცელო")