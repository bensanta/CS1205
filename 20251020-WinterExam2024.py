# Question 2

# (a) Create a function that takes as input a string and returns another string that
# contains the first character of the input string followed by the last character of
# the input string, followed by the last two digits of your student number.


def ReturnString(input):
    return input[:1] + input[len(input)-1:] + str(65)

print(ReturnString("hello"))


# (b) Create a code in Python - it does not need to be a function - to read day,
# month and year of birth of a person and calculate and print how old that person is Today.

birth_year = int(input("The year you were born (eg. 2006): "))
birth_month = int(input("The month you were born (eg. 01): "))
birth_day = int(input("The day you were born (eg. 16): "))

