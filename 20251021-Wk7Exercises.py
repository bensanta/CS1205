"""
Week 7 Exercise list - https://ucc.instructure.com/courses/83383/pages/week-7-lab-exercises-functions?module_item_id=2776505
"""

"""
Question 1

Students in a course submit 3 assignments and have 1 exam.
All are graded 1-100, but the sum of the assignments weighs 30% of the final mark and the exam weighs 70%.
All marks, including the final mark, are integer numbers.
Define a function to calculate and return the final mark. It returns -1 if any of the marks is out of range.
Test your function thoroughly.
"""

def FinalGrade(assignment1, assignment2, assignment3, exam):
    # if ((assignment1 or assignment2 or assignment3 or exam) < 1) or((assignment1 or assignment2 or assignment3 or exam) > 100):
    #     return -1
    if (assignment1 < 1 or assignment2 < 1 or assignment3 < 1 or exam < 1 or #checks less than 1
            assignment1 > 100 or assignment2 > 100 or assignment3 > 100 or exam > 100): #checkks more than 100
        return -1
    else:
        finalScore = ((assignment1 + assignment2 + assignment3) * .3) + (exam * .7)
        return int(finalScore)

# testing
# print(FinalGrade(0,17,87,79)) #should return -1
# print(FinalGrade(100,100,100,100))
# print(FinalGrade(100,100,101,100)) #should return -1



"""
Question 2
Define a function to find the smallest of three numbers.  Test it.
"""

def SmallestNum(a, b, c):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return a
    else:
        return c # it could also be formatted like that if requesting a string output --> "%d is the smallest value" % c

# testing
# print(SmallestNum(1, 83, 90))
# print(SmallestNum(89, 83, 90))
# print(SmallestNum(89, 83, 5))

"""
Question 3
Define a function to find the largest of three numbers. Test it.
"""

def LargestNum(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

# testing
# print(LargestNum(4, 2, 3))
# print(LargestNum(4, 8, 3))
# print(LargestNum(4, 8, 100))


"""
Question 4

4 - Define two different functions to return the range between three numbers, that is, the largest and the smallest of three numbers. 
4.1 - The first function does so by calling the functions defined in exercises 2 and 3.
4.2 - The second function codes conditionals from scratch to define the range. 
Obs. Python allows you to return more than one value in a function. You just have to list them in the return command.
"""

def FindDifference1(a, b):
    if a > b:
        return a - b
    elif a < b:
        return b - a
    else:
        return 0

print(FindDifference1(LargestNum(1,2,4),SmallestNum(9,4,3)))


def FindDifference2(a, b, c):
    #find largest num from the 3
    largest = 0
    if a > b and a > c:
        largest = a
    elif b > a and b > c:
        largest = b
    else:
        largest = c

    # find smallest num from the 3
    smallest = 0
    if a < b and a < c:
        smallest = a
    elif b < a and b < c:
        smallest = b
    else:
        smallest = c

    return largest - smallest

print(FindDifference2(6,4,2)) # 6-2=4
print(FindDifference2(2,8,5)) # 8-2=6
print(FindDifference2(9,8,5)) # 9-5=4

# my own practice below just for fun!

# Add one number after the other, so if the input to x is 4, the algorithm should return 10. because 1+2+3+4 is 10.
def addToX(x):
    currentLoop = 0
    totalSum = 0
    while currentLoop != (x+1):
        totalSum = totalSum + currentLoop
        currentLoop += 1
    return totalSum

print(addToX(4))
print(addToX(13))
print(addToX(14))

# now doing one with just even numbers: # Add one number after the other, so if the input to x is 4, the algorithm should return 6. because 2+4 is 6.
def addToXEven(x):
    currentLoop = 0
    totalSum = 0
    while currentLoop != (x + 1):
        if currentLoop % 2 == 0:
            totalSum = totalSum + currentLoop
        currentLoop += 1
    return totalSum

print(addToXEven(4))
print(addToXEven(13))
print(addToXEven(14))
print(addToXEven(15))
print(addToXEven(16))


#Rachel Help

def calculateBMI(kg, meter):
    return (kg/(meter)**2)

print(calculateBMI(63,1.57))

print(5/3.281)
print(2/39.37)

def HeightConversion (feet, inches):
    return (feet/3.281)+ (inches/39.37)

print(HeightConversion(5, 2))

def WeightConversion (stones, lbs):
    return (stones*6.35)+ (lbs/2.205)


def WeightClassification (bmi):
    classification=""

    if bmi<18.5:
        classification= "underweight"
    elif bmi >=18.5 and bmi<25.0:
        classification="healthy weight"
    elif bmi>=25.0 and bmi<30.0:
        classification="overweight"
    elif bmi>=30.0 and bmi<35.0:
        classification="obesity I"
    elif bmi>=35.0 and bmi<40:
        classification="obesity II"
    elif bmi>=40:
        classification="obesity III"

    return classification
















