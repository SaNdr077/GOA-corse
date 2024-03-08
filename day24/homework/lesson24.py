#1)
"""You were camping with your friends far away from home,
but when it's time to go back, you realize that
your fuel is running out and the nearest pump is 50 miles away!
You know that on average, your car runs on about 25 miles per gallon.
There are 2 gallons left.
Considering these factors, write a function that tells you if it is possible to get to the pump or not.
Function should return true if it is possible and false if not."""

def zero_fuel(distance_to_pump, mpg, fuel_left):
    if distance_to_pump / mpg <= fuel_left:
        return True
    return False

print (zero_fuel(50, 25, 2))



#2)
# Write a function to split a string and convert it into an array of words.
# Examples (Input ==> Output):

def string_to_array(s):
    return s.split(" ")

print(string_to_array("Robin Singh"))


#3) 7kyu
"""Return the number (count) of vowels in the given string.
We will consider a, e, i, o, u as vowels for this Kata (but not y).
The input string will only consist of lower case letters and/or spaces."""


def get_count(sentence):
    result = 0
    for i in sentence:
        if i in "aeiou":
            result += 1
    return result

print (get_count("aeiou"))

#4) 7kyu
"""Trolls are attacking your comment section!
A common way to deal with this situation is to remove all of the vowels
 from the trolls' comments, neutralizing the threat.
Your task is to write a function that takes a string and return
 a new string with all vowels removed.
 For example, the string "This website is for losers LOL!" 
would become "Ths wbst s fr lsrs LL!".
Note: for this kata y isn't considered a vowel."""

def disemvowel(string_):
    result = ""
    for char in string_:
        if char not in "aeiouAEIOU":
            result += char
    return result

print (disemvowel("aeiou"))

#5) 7kyu
"""Welcome. In this kata, you are asked to square 
every digit of a number and concatenate them.
For example, if we run 9119 through the function,
 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)
Example #2: An input of 765 will/should return 493625
 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)
Note: The function accepts an integer and returns an integer.
Happy Coding!"""

def square_digits(num):
    square = ""
    arr = str(num).split(", ")
    for i in arr:
        for char in i:
            square += str(int(char) * int(char))
    return int(square)

print(square_digits(9119))

#6) 7kyu 
"""
In this little assignment you are given a string of space separated numbers,
 and have to return the highest and lowest number.
Examples
high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"
"""

def high_and_low(numbers):
    result = ""
    arr = str(numbers).split(" ")
    my_arr = []
    for i in arr:
        my_arr.append(int(i))
    result += str(max(my_arr)) + " " 
    result += str(min(my_arr)) 
    return (result)

print (high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))