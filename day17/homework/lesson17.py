#1) Given a non-empty array of integers, 
# return the result of multiplying the values
# together in order. Example:
# [1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24

def grow(arr):
    num = 1
    for i in arr:
        num *= i
    return num
print (grow([4, 1, 1, 1, 4]))  




#2) Given an array of integers.
# Return an array, where the first element is the count 
# of positives numbers and the second element is sum of 
# negative numbers. 0 is neither positive nor negative.
# If the input is an empty array or is null, return an empty array.
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15],
# you should return [10, -65].

def count_positives_sum_negatives(arr):
    number = [0, 0]
    num = []
    for i in arr:
        if i > 0:
            num.append(i)
            for char in range(len(num)+1):
                number[0] = char
        elif i < 0:
            number[1] += i
    if arr == []:
        del(number[0:])
    return number
print (count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]))

#3) There was a test in your class and you passed it. Congratulations!
# But you're an ambitious person. You want to know if you're better 
# than the average student in your class.
# You receive an array with your peers' test scores.
#  Now calculate the average and compare your score!
# Return True if you're better, else False!
# Note:
# Your points are not included in the array of your class's points. For 
# calculating the average point you may add your point to the given array!

def better_than_average(class_points, your_points):
    class_points.append(your_points)
    total_score = 0
    student_quantity = 0
    for i in class_points:
        total_score += i
        student_quantity += 1
        averange = total_score / student_quantity
    if averange <= your_points:
        return True
    return False