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

    #ERROR HANDLING
    if height < 0 or weight < 0:
        #f-string with if...else - https://www.w3schools.com/python/python_string_formatting.asp
        return f"{'HEIGHT' if height < 0 else ''}{' and ' if height < 0 and weight < 0 else ''}{'WEIGHT' if weight < 0 else ''} should not be below 0"

    return float(weight / (height ** 2)) #for some reason has to be typecast. it kicked up a fuss without the casting in Q4

# ToDO Thorough Testing on BMI Calc
print("\n\nQuestion 1: BMI Calculations")

# --- Tests with expected BMI values ---
print(calculateBMI(1.3, 9))        # expect: 5.3290705182
print(calculateBMI(1.80, 75))      # expect: 23.1481481481
print(calculateBMI(1.0, 1))        # expect: 1.0
print(calculateBMI(2.5, 50))       # expect: 8.0
print(calculateBMI(1.75, 0))       # expect: 0.0
print(calculateBMI(0.5, 10))       # expect: 40.0
print(calculateBMI(0.001, 60))     # expect: 60000000.0

# --- Error handling tests ---
print(calculateBMI(-1.75, 70))     # expect: "HEIGHT should not be below 0"
print(calculateBMI(1.75, -70))     # expect: "WEIGHT should not be below 0"
print(calculateBMI(-1.75, -70))    # expect: "HEIGHT and WEIGHT should not be below 0"

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
        return f"ERROR: You entered {inches} inches. Please enter a value between 0 and <12 inches. 12 inches is a whole new feet."
    elif feet < 0: #negative stones not realistic
        return f"ERROR: You entered {feet} feet. Please enter a positive value of feet in length, as it's not possible to have negative length."

    # Conversion
    return (feet / 3.281) + (inches / 39.37)

# TODO: the height conversion as much as possible

print("-------------\n-------------\nQuestion 2.1: Imperial Height to Metric Tests")

print(heightToMetric(6, 20))    # Returns the error
print(heightToMetric(6, 1))     # valid
print(heightToMetric(9, 10))    # valid
print(heightToMetric(5, 5))     # valid
print(heightToMetric(5, 14))    # inches > 12 -> Returns the error
print(heightToMetric(5, -15))    # negative inches -> Returns the error
print(heightToMetric(5, 8))     # valid
print(heightToMetric(6, 2))     # valid

print(heightToMetric(5, 12))     # inches == 12 -> ERROR - 12 inches is a whole new feet
print(heightToMetric(5, 13))     # inches more than 12 -> ERROR

print(heightToMetric(-1, 5))     # negative feet -> ERROR
print(heightToMetric(5, -1))     # negative inches -> ERROR

print(heightToMetric(5.5, 0))    # valid - fractional feet -> expect 1.676
print(heightToMetric(0, 5.5))    # valid - fractional inches -> expect 0.140

print(heightToMetric(0, 0))      # valid - zero height -> expect 0.0
print(heightToMetric(0, 11.99))  # valid - edge of inch range -> expect 0.305





def weightToMetric(stones, pounds):
    # BOUNDARIES: There are only 14 pounds in a stone - https://stone-synergy.co.uk/how-many-pounds-in-a-stone/
    if pounds < 0 or pounds >= 14:
        return f"ERROR: You entered {pounds} pounds. Please enter a value between 0 and 13 pounds."
    elif stones < 0: #negative stones not realistic
        return f"ERROR: You entered {stones} stones. Please enter a positive value of stones in weight, as it's not possible to have negative weight."

    #To counteract the rounding issue
    # Exact values from https://www.unitconverters.net/weight-and-mass/lbs-to-kg.htm
    # British Imperial unit of mass:  https://en.wikipedia.org/wiki/Avoirdupois
    return (stones * 6.35029318) + (pounds / 2.2046226218)

# TODO: the weight conversion as much as possible
# --- Tests ---
print("-------------\n-------------\nQuestion 2.2: Imperial Weight to Metric Tests")

print(weightToMetric(0, 0))         # expect: 0.0
print(weightToMetric(0, 13))        # expect: 5.8967008101304605
print(weightToMetric(0, -1))         # expect: return weight error for negative pounds
print(weightToMetric(0, 14))        # expect: return weight error for pounds over 13 -> 14 pounds makes a new stone

print(weightToMetric(1, 0))         # expect: 6.35029318
print(weightToMetric(1, 7))         # expect: 9.52543
print(weightToMetric(2, 13))        # expect: 18.5972

print(weightToMetric(11, 0))        # expect: 69.8532
print(weightToMetric(11, 3))        # expect: 71.214
print(weightToMetric(15, 13))       # expect: 101.1510
print(weightToMetric(100, 0))       # expect: 635.029318

# Negative stones now trigger
print(weightToMetric(-1, 5))           # expect: "ERROR: You entered -1 stones. Please enter a positive value of stones in weight, as it's not possible to have negative weight."

# --- Fractional values for stones and pounds --- -> it was never said stones or MUST be an integer. therefore decimals must be tested
print(weightToMetric(0.5, 0))          # expect: 3.17514
print(weightToMetric(0.25, 7))         # expect: 4.9002
print(weightToMetric(1.5, 0))          # expect: 9.5254
print(weightToMetric(2.5, 3.5))        # expect: 16.2613
print(weightToMetric(7.25, 6.5))       # expect: 47.0352
print(weightToMetric(0.75, 13.25))     # expect: 10.0293
print(weightToMetric(10.5, 13.9))      # expect: 71.3857



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
