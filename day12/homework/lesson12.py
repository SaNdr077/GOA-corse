#1) Given a set of numbers,
# return the additive inverse of each. Each 
# positive becomes negatives, and the negatives become positives.

def invert(lst):
    my_arr = []
    for i in lst:
        if i > 0:
            my_arr.append(-i)
        else:
            my_arr.append(-i)
    return my_arr
print (invert([1,2,3,4]))

#2) Write a function which calculates the 
# average of the numbers in a given list.
# Note: Empty arrays should return 0.

def find_average(numbers):
    num = 0
    for i in numbers:
        num += i
    if numbers == []:
        return 0
    return num / (len(numbers))
print (find_average([1,5,7]))
    
#3) A hero is on his way to the castle to complete his mission.
# However, he's been told that the castle is surrounded with 
# a couple of powerful dragons! each dragon takes 2 bullets to
# be defeated, our hero has no idea how many bullets he should carry..
# Assuming he's gonna grab a specific given number of bullets and move 
# forward to fight another specific given number of dragons,
# will he survive?
# Return true if yes, false otherwise :)

def hero(bullets, dragons):
    if bullets >= (2 * dragons):
        bullets % 2 == 0 and dragons % 2 == 0
        return True
    return False
print(hero(11, 7))