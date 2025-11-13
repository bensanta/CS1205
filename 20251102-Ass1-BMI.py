"""
Assignment 1
CS1205 UCC AY2025
@author BSanta
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

# TODO: add error handling return codes

"""
Error codes and meanings:
10001: Negative Height
10002: Negative Weight
10003: Negative Height AND Weight
10004: Invalid BMI
"""


# TODO: allow inches over 12, and allow lbs over 14. no reason to complicate further.

def calculateBMI(height, weight):
    # calculate bmi formulae: kg/m^2 - https://www.diabetes.ca/resources/tools-resources/body-mass-index-(bmi)-calculator
    # Example
    # height: 1.80 -> 180cm / 1.8m
    # weight: 75 -> 75kg

    #ERROR HANDLING
    if height < 0 and weight < 0:
        return 10003
    elif height < 0:
        return 10001
    elif weight < 0:
        return 10002

    return float(weight / (height ** 2)) #for some reason has to be typecast. it kicked up a fuss without the casting in Q4


print("-------------\n-------------\nQuestion 1: BMI Calculations")

# --- Tests with expected BMI values ---
print(calculateBMI(-1.3, 9))        # expect: ERR 10001
print(calculateBMI(1.3, -9))        # expect: ERR 10002
print(calculateBMI(-1.3, -9))        # expect: ERR 10003
print(calculateBMI(1.3, 9))        # expect: 5.3290705182
print(calculateBMI(1.80, 75))      # expect: 23.1481481481


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

    if ((feet / 3.281) + (inches / 39.37)) < 0:
        return 10001

    # Conversion
    return (feet / 3.281) + (inches / 39.37)


print("\n-------------\n-------------\nQuestion 2.1: Imperial Height to Metric Tests")

print(heightToMetric(6, 20))    # Returns the error
print(heightToMetric(6, 1))     # valid
print(heightToMetric(-6, 1))     # err
print(heightToMetric(-6, -1))     # err
print(heightToMetric(6, -1))     # valid
print(heightToMetric(6, -100))     # err



def weightToMetric(stones, pounds):

    if ((stones * 6.35029318) + (pounds / 2.2046226218)) < 0:
        return 10002

    #To counteract the rounding issue
    # Exact values from https://www.unitconverters.net/weight-and-mass/lbs-to-kg.htm
    # British Imperial unit of mass:  https://en.wikipedia.org/wiki/Avoirdupois
    return (stones * 6.35029318) + (pounds / 2.2046226218)

# TODO: the weight conversion as much as possible
# --- Tests ---
print("\n-------------\n-------------\nQuestion 2.2: Imperial Weight to Metric Tests")

print(weightToMetric(0, 0)) # expect: 0.0
print(weightToMetric(1,-15)) #err
print(weightToMetric(-1,15)) #valid
print(weightToMetric(-10,15)) #err
print(weightToMetric(-1,-15)) #err
print(weightToMetric(1,15)) #valid -> no reason to limit pounds to only 1->14
print(weightToMetric(13,10)) #valid
print(weightToMetric(13,30)) #valid



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

    #ERR Handling
    if bmi == 10001:
        return 10001
    elif bmi == 10002:
        return 10002
    elif bmi == 10003:
        return 10003

    # these classifications are from the above linked assignment
    if bmi <= 0:
        return 10004 #negative bmi OR 0
    elif bmi > 0 and bmi < 18.5:
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
    else: #todo: add error codes into here, specific == like bmi == 10001 then height err, etc
        classification = "obese class III"
        health_problems_risk = "extremely high"

    # Print an output for the user - using f-string to make it more elegant -
    # https://www.w3schools.com/python/python_string_formatting.asp
    return (f"With a BMI of {round(bmi,2)} you are {classification} with {health_problems_risk} risk of developing "
            f"health problems.")



print("\n-------------\n-------------\nQuestion 3: BMI Risk Factor Tests")

print(bmiRiskFactor(0)) #ERR
print(bmiRiskFactor(-1)) #ERR

# UNDERWEIGHT (<18.5)
print(bmiRiskFactor(0.1)) #valid, technically underweight
print(bmiRiskFactor(18.49))
print(bmiRiskFactor(10))

# NORMAL (18.5–24.9)
print(bmiRiskFactor(18.5))
print(bmiRiskFactor(24.99))

# OVERWEIGHT (25–29.9)
print(bmiRiskFactor(25))
print(bmiRiskFactor(29.99))

# OBESE CLASS I (30–34.9)
print(bmiRiskFactor(30))
print(bmiRiskFactor(34.99))

# OBESE CLASS II (35–39.9)
print(bmiRiskFactor(35))
print(bmiRiskFactor(39.99))

# OBESE CLASS III (≥40)
print(bmiRiskFactor(40))
print(bmiRiskFactor(60))




"""
Question 4: Imperial BMI Classification

            Finally, define and test a function in Python that takes the height and weight of a person
            (in Imperial scale) and returns the weight classification of that person, BY CALLING
            YOUR FUNCTIONS ABOVE to convert height and weight to metric, calculate BMI and
            give weight classification as a result.
            
            Example: Say your function prototype is:
            patient_weight_classification (feet, inches, stones, pounds).
"""

def patientWeightClassification (feet, inches, stones, pounds):

    # needed for the err handling calcs - additions have to be done, because technically -1 foot but 15 inches could
    # still work

    height = (feet / 3.281) + (inches / 39.37)
    weight = (stones * 6.35029318) + (pounds / 2.2046226218)

    #ERROR HANDLING
    if calculateBMI(height, weight) < 0: #error handle for BMI specifically
        return 10004
    elif height < 0 and weight < 0:
        return 10003
    elif height < 0:
        return 10001
    elif weight < 0:
        return 10002


    # TODO explain how this return works
    return bmiRiskFactor(calculateBMI(heightToMetric(feet, inches), weightToMetric(stones, pounds)))

#TODO: test thoroughly - all edge cases, and all fails / errors too.

print("\n-------------\n-------------\nQuestion 4: patientWeightClassification tests")

#ERRs
print(patientWeightClassification(-10,10,-3,2))
print(patientWeightClassification(10,10,-3,2))
print(patientWeightClassification(-10,10,3,2))

# Underweight (<18.5)
print(patientWeightClassification(6, 0, 9.70, 0))         # expect: underweight / increased risk

# Normal (==18.5 lower edge, and <25 upper edge)
print(patientWeightClassification(6, 0, 9.7434, 0))       # expect: normal weight / less risk (edge at 18.5)
print(patientWeightClassification(6, 0, 13.15, 0))        # expect: normal weight / less risk (just below 25)

# Overweight (==25 lower edge, and <30 upper edge)
print(patientWeightClassification(6, 0, 13.1668, 0))      # expect: overweight / increased risk (edge at 25)
print(patientWeightClassification(6, 0, 15.78, 0))        # expect: overweight / increased risk (just below 30)

# Obese class I (==30 lower edge, and <35 upper edge)
print(patientWeightClassification(6, 0, 15.8001, 0))      # expect: obese class I / high risk (edge at 30)
print(patientWeightClassification(6, 0, 18.41, 0))        # expect: obese class I / high risk (just below 35)

# Obese class II (==35 lower edge, and <40 upper edge)
print(patientWeightClassification(6, 0, 18.4335, 0))      # expect: obese class II / very high risk (edge at 35)
print(patientWeightClassification(6, 0, 21.04, 0))        # expect: obese class II / very high risk (just below 40)

# Obese class III (>=40)
print(patientWeightClassification(6, 0, 21.0668, 0))      # expect: obese class III / extremely high risk (edge at 40)
print(patientWeightClassification(6, 0, 23.0, 0))         # expect: obese class III / extremely high risk


