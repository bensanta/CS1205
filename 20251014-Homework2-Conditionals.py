# https://ucc.instructure.com/courses/83383/pages/lab-week-6-exercises-conditionals?module_item_id=2769168


# Q1: BMI Calculations


def BMI_Risk_Factor(height, weight):
    # calculate bmi formulae: kg/m^2 - https://www.diabetes.ca/resources/tools-resources/body-mass-index-(bmi)-calculator
    # Example
    # height: 1.80
    # weight: 75
    bmi = weight/(height**2)

    classification = ""
    health_problems_risk = ""
    if bmi < 18.5:
        classification = "underweight"
        health_problems_risk = "increased"
    elif bmi >= 18.5 and bmi < 25:
        classification = "normal weight"
        health_problems_risk = "least"
    elif bmi >= 25 and bmi < 30:
        classification = "overweight"
        health_problems_risk = "increased"
    elif bmi >= 30 and bmi < 35:
        classification = "obese class I"
        health_problems_risk = "high"
    elif bmi >= 35 and bmi < 40:
        classification = "obese class II"
        health_problems_risk = "very high"
    else:
        classification = "obese class III"
        health_problems_risk = "extremely high"

    # Print an output for the user
    print("With a BMI of", round(bmi, 2), "you are", classification, "with", health_problems_risk, "risk of developing health problems")

"""# test BMI
BMI_Risk_Factor(1.80, 182.9)
BMI_Risk_Factor(.80, 182.9)"""

# Q2: Write Python code to calculate the largest value between a, b, and c.
# Preset your a, b and c values to test the code. No need to read from the user.

def Max_Value(a, b, c):

    # check if A is the largest
    if a > b and a > c:
        print(a, "is the largest out of the three values")

    # check if B is the largest
    if b > a and b > c:
        print(b, "is the largest out of the three values")

    # check if C is the largest
    if c > a and c > b:
        print(c, "is the largest out of the three values")


"""
Max_Value(4, 5, 6)
Max_Value(8, 5, 6)
Max_Value(8, 12, 6)
Max_Value(0, 0, 0) # assignment didn't ask to check equal values
Max_Value(8, 10, 45)
"""

# Q3:
    # Assignments each graded 1 to 10
    # Attendance given a percentage, so a value between 0 and 1
    #   EG: 50% is 0.5

def Final_Grade(assignment1, assignment2, assignment3, assignment4, attendance):
    studentMark = ""
    assignmentScoreSum = assignment1 + assignment2 + assignment3 + assignment4

    if attendance < .5 or assignmentScoreSum < 20:
        studentMark = "FAIL"
    else:
        if assignmentScoreSum >= 20:
            studentMark = "PASS"
        if assignmentScoreSum >= 30:
            studentMark = "PASS"

    # final output
    if assignmentScoreSum >= 30 and attendance >= 0.6:
        print("This student receives a PASS and a commendation of GREAT ACHIEVEMENT as their assignment scored", assignmentScoreSum, "and they had an attendance of over 60%.")
    elif attendance < 0.5:
        print("This student receives a FAIL, as their attendance unfortunately is only " + str(attendance*100) + "% and the mininmum passing requirement is 50%")
    else:
        print("This student receives a", studentMark, "as their assignment scored", assignmentScoreSum)


# Final_Grade(10,10,10,10,1)
# Final_Grade(0,10,0,10,1)
# Final_Grade(0,8,0,10,1)
# Final_Grade(10,10,10,10,.4)


#Rach hw help
print(3 % 2) # 1

print(20 % 15) # 5

print(10 % 8) # 2

print(14 % 9) # 5

print(20 % 2) # 0

print(6 % 3) # 0