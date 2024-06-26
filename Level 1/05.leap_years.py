'''
In this example we use if statements and functions to see if a year is a leap year or not.

Leap years in the Gregorian calendar are based around the follow facts:
    Tropical Year = 365.252422 days
    Gregorian calendar adds 1 day every 4 years
                       adds 1 day every 400 years
    which equates to 365 + 1/4 + 1/400 = 365.2525 days

    Thus we need leap years every 4th year and every 4th century

Examples:
    2000        is a leap year      (5 * 400)
    2003        is NOT a leap year  (not divisible by 4)
    2024        is a leap year      (506 * 4)
    2100        is NOT a leap year  (divisible by 100)
'''

print("Days in Gregorian Year:", 365 + 1/4 + 1/400)

# year = int(input("Enter a year: "))

def isLeapYear(year):
    isLeap = False
    if year % 4 == 0: isLeap = True
    if year % 100 == 0: isLeap = False
    if year % 400 == 0: isLeap = True
    if isLeap:
        return f"{year} is a Leap Year"
    else:
        return f"{year} is NOT a Leap Year"

# def isLeapYear(year):
#     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#         return f"{year} is a Leap Year"
#     else:
#         return f"{year} is NOT a Leap Year"

print(isLeapYear(2000))
print(isLeapYear(2003))
print(isLeapYear(2024))
print(isLeapYear(2100))

