"""
Assignment 1
CS1205 UCC AY2025
@author Benjamin Santa
Assignment Link: https://ucc.instructure.com/courses/83383/files/9598932?wrap=1
"""

"""
Question 1: BMI (Body Mass Index) Calculator
            BMI is a number that can be calculated from someone’s height (in
            meters) and weight (in kg), and will give as a result a value, whose range indicates a
            weight classification
            
            The formula for BMI is given by:
            BMI = weight(kg)/height(meters)^2
            
            Define YOUR OWN Python function that has as parameters a user a height value
            (floating point, in meters) and weight (floating point, in kilograms), and returns the
            corresponding BMI.
            
            Write code in your main program to properly test your function with preset variables in
            the main program.
"""
def calculateBMI(height, weight):
    # calculate bmi formulae: kg/m^2 - https://www.diabetes.ca/resources/tools-resources/body-mass-index-(bmi)-calculator
    # Example
    # height: 1.80 -> 180cm / 1.8m
    # weight: 75 -> 75kg
    return float(weight / (height ** 2))

# ToDO Thorough Testing on BMI Calc

"""
Question 2: Imperial to Metric Conversion
            Height: Convert height (in Imperial scale) to metric. This function takes the number of feet
                    and the number of inches as parameters and returns the height in meters (floating-
                    point).
            Weight: Convert weight (in Imperial scale) to metric. This function takes the number of
                    stones and the number of pounds (both integers) as parameters and returns the
                    weight in kilograms (floating-point).
"""

def heightToMetric(feet, inches):
    # BOUNDARIES: inches > 12 - https://www.rapidtables.com/convert/length/inch-to-feet.html
    if inches < 0 or inches >= 12: # because 12 inches is a whole new feet
        return f"ERROR: You entered {inches} inches. Please enter a value between 0 and 12 inches."

    # Conversion
    return (feet / 3.281) + (inches / 39.37)

# TODO: the height conversion as much as possible


print(heightToMetric(6, 20)) #Returns the error
print(heightToMetric(6, 1))
print(heightToMetric(9, 10))
print(heightToMetric(5, 5))
print(heightToMetric(5, 14)) #Returns the error
print(heightToMetric(5, -15)) #Returns the error

def weightToMetric(stones, pounds):
    # BOUNDARIES: There are only 14 pounds in a stone - https://stone-synergy.co.uk/how-many-pounds-in-a-stone/
    if pounds < 0 or pounds >= 14:
        return f"ERROR: You entered {pounds} pounds. Please enter a value between 0 and 13 pounds."

    #To counteract the rounding issue
    # Exact values from https://www.unitconverters.net/weight-and-mass/lbs-to-kg.htm
    # British Imperial unit of mass:  https://en.wikipedia.org/wiki/Avoirdupois
    return (stones * 6.35029318) + (pounds / 2.2046226218)

# TODO: the weight conversion as much as possible

print("\nWeight Conversion:")
print(weightToMetric(14, 5))
print(weightToMetric(18, 2))



"""
Question 3: Determining Health Risks Based on BMI
            Write a Python function that receives a value of BMI as the parameter (floating point) and
            returns a string for the weight classification corresponding to that BMI value, according
            to Table 1.
            
            Test your function properly with values in all ranges and on the borders of the ranges.
            Use only pre-set variables in your program in your submitted code. Remember: no input
            from the user.
            
            Print all results in your main program.
"""

# Below code taken from previous homework:
# https://github.com/bensanta/CS1205/blob/be101153d4cdc3e8c6a67e099ad7cb4be366089e/20251014-Homework2-Conditionals.py
def bmiRiskFactor(bmi):
    # Declare variables needed within the ifs below
    classification = ""
    health_problems_risk = ""

    # these classifications are from the above linked assignment
    if bmi < 18.5:
        classification = "underweight"
        health_problems_risk = "increased"
    elif bmi >= 18.5 and bmi < 25:
        classification = "normal weight"
        health_problems_risk = "less"
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

    # Print an output for the user - using f-string to make it more elegant - https://www.w3schools.com/python/python_string_formatting.asp
    return f"With a BMI of {round(bmi,2)} you are {classification} with {health_problems_risk} risk of developing health problems."



# ToDo - testing of all 6 categories AND the boundaries, for example bmi=40 and bmi=25 and bmi=18.5 and bmi=18.49

# Testing output of all 6 categories
# print(bmiRiskFactor(calculateBMI(1.8, 50)))
# print(bmiRiskFactor(calculateBMI(1.8, 70)))
# print(bmiRiskFactor(calculateBMI(1.8, 90)))
# print(bmiRiskFactor(calculateBMI(1.8, 100)))
# print(bmiRiskFactor(calculateBMI(1.8, 120)))
# print(bmiRiskFactor(calculateBMI(1.8, 130)))


"""
Question 4: Imperial BMI Classification

            Finally, define and test a function in Python that takes the height and weight of a person
            (in Imperial scale) and returns the weight classification of that person, BY CALLING
            YOUR FUNCTIONS ABOVE to convert height and weight to metric, calculate BMI and
            give weight classification as a result.
            
            Example: Say your function prototype is:
            patient_weight_classification (feet, inches, stones, pounds).
"""

#TODO: get parameters input of (ft, in, st, lb)
#TODO: then use the conversion function and be like height=heightToMetric(ft, in)
#TODO: then use the conversion function and be like weight=weightToMetric(st, lb)
#TODO: pass all values through calculateBMI(height, weight) -> calculateBMI(heightToMetric(ft, in), weightToMetric(st, lb))
#TODO: Pass BMI through bmiRiskFactor(bmi) -> bmiRiskFactor(calculateBMI(heightToMetric(ft, in), weightToMetric(st, lb)))

def patientWeightClassification (feet, inches, stones, pounds):

    # TODO: add in some error handling - same logic as before for inches and pounds
    return bmiRiskFactor(calculateBMI(heightToMetric(feet, inches), weightToMetric(stones, pounds)))

#TODO: test thoroughly - all edge cases, and all fails too.

print("\nQuestion 4:")
print(patientWeightClassification(5, 10, 11.4286, 0))
