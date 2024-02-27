#1) მომხმარებელს კითხეთ თავისი ასაკი და მამის ასაკი და დაუპრინტეთ
# ყოველ წელს რამდენზერ დიდი იქნება მამა შვილზე

mather_age = int(input("enter your mather age: "))
your_age = int(input("enter your age: "))
year = int(input("enter year: "))
for i in range (100):
    print (year + i, "year", "he will be bigger then you",(mather_age + i)/(your_age + i))

#2) 0 დან 30მდე დაპრინტეთ ყველა ლუწი და კენტი 
# რიცხვი და გვერძე მიუწერეთ ლუწია თუ კენტი
i = 30
while i > 0:
    if i % 2 == 0:
        print (i, "even")
    else:
        print (i, "odd")
    i -= 1
    