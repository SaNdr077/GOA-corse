#1)
"""Write a function that takes an array of words and smashes
them together into a sentence and returns the sentence.
You can ignore any need to sanitize words or add punctuation,
but you should add spaces between each word. Be careful, 
there shouldn't be a space at the beginning 
or the end of the sentence!"""

# def smash(words):
#     new_words = " ".join(words)
#     return new_words

# print (smash(['hello', 'world', 'this', 'is', 'great']))


#2)
'''Write function bmi that calculates body mass index (bmi = weight / height2).
if bmi <= 18.5 return "Underweight"
if bmi <= 25.0 return "Normal"
if bmi <= 30.0 return "Overweight"
if bmi > 30 return "Obese"'''

def bmi(weight, height):
    bmi = weight / (height * height)
    if bmi <= 18.5:
        return "Underweight"

    elif bmi <= 25.0:
        return "Normal"

    elif bmi <= 30.0:
        return "Overweight"

    elif bmi > 30:
        return "Obese"
    
#3
"""Your task is to make two functions 
( max and min, or maximum and minimum, 
etc., depending on the language ) that receive a list 
of integers as input, and return the largest and lowest 
number in that list, respectively.
Examples (Input -> Output)"""


def minimum(arr):
    number_min = min(arr)
    return number_min
print(minimum([-52, 56, 30, 29, -54, 0, -110]))
def maximum(arr):
    number_max = max(arr)
    return number_max
print(maximum([-52, 56, 30, 29, -54, 0, -110]))

#4
"""Given a string of digits, you should replace any digit
 below 5 with '0' and any digit 5 and above with '1'. 
 Return the resulting string.
Note: input will never be an empty string"""
def fake_bin(x):
    result = ""
    for i in x:
        if int(i) >= 5:
            result += "1"
        elif int(i) < 5:
            result += "0"
    return result
print (fake_bin("15645158489"))

#5
"""You will be given an array a and a value x.
 All you need to do is check whether the provided 
 array contains the value.
Array can contain numbers or strings. X can be either.
Return true if the array contains the value, false if not."""


def check(seq, elem):
    for element in seq:
        if element == elem:
            return True
    return False
print (check(["what", "a", "great", "kata"], "kata"))

#6 
"""Create a function which translates a given DNA string into RNA.
For example:
"GCAT"  =>  "GCAU"
The input string can be of arbitrary length - in particular,
 it may be empty. All input is guaranteed to be valid, 
 i.e. each input string will only ever consist of 'G', 'C', 'A' and/or 'T'."""


def dna_to_rna(dna):
    dna = dna.replace("T", "U")
    return dna
print (dna_to_rna("TTTT"))





                
        