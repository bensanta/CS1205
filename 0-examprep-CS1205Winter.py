"""
CS 1205 Winter Exam Prep
"""

"""
Create a code in Python - it does not need to be a function - to read DAY, MONTH and YEAR of birth of a person and 
calculate and print how old that person is Today.
"""

birthYear = int(input("Enter your birth year (YYYY): "))
# birthMonth = int(input("Enter your birth month (MM): "))
# birthDay = int(input("Enter your birth day (DD): "))

todayYear = int(input("Enter today's year (YYYY): "))
# todayMonth = int(input("Enter today's month (MM): "))
# todayDay = int(input("Enter today's day (DD): "))

dayCount = 0
leapYears = 0
while birthYear-1 != todayYear:
    if birthYear % 4 == 0:
        leapYears += 1
    birthYear += 1
    print(birthYear,leapYears)

print(leapYears)
