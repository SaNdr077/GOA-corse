# 1)
proposal = input("enter proposal: ")
for i in proposal:
    if i not in "aeiou":
        print(i)

# 2) 
surname1 = input("enter your first surname1: ")
surname2 = input("enter your first surname2: ")
more_consent1 = 0
more_consent2 = 0
for char in surname1:
    if char in "a":
        more_consent1 +=1
for char in surname2:
    if char in "a":
        more_consent2 +=1
if more_consent1 > more_consent2:
    print (surname1)
elif more_consent1 < more_consent2:
    print (surname2)
else:
    print("equel")




# 3)
boy = ["ushangi", "jemala", "valiko", "bichiko"]
gerl = ["marusa", "mayvala", "lela", "nina"]
i = 0
while i < len(boy):
    print ("couples ", boy[i] +"-"+ gerl[i])
    i += 1

my_list = ["sakartvelo", "itali", "chineti"]

chineti = len (my_list[0])
sakartvelo =len (my_list[1])
itali =len (my_list[2])

if chineti > sakartvelo and chineti < itali:
    print (my_list[0])
elif sakartvelo > chineti and sakartvelo < itali:
    print (my_list[1])         
else:
    print (my_list[2])