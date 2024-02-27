# მომხმარებელს კითხეთ სახელი და ასაკი და დაუპრინტეთ
# ასაკი: შენ იქნები 24 წლის 2024 წელს
#        შენ იქნები 25 წლის 2025 წელს

name = input("enter your name: ")
age = int(input("enter your age: "))
year = 2024
for i in range(age):
    print("my name:", name, "your age:", age + i, "will be:", year + i, "this year")



seats = 10
while seats > 0:
    print(seats, "sell ticket")
    seats = seats - 1