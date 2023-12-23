'''
5.15 LAB: Seasons
Write a program that takes a date as input and outputs the date's season in the northern hemisphere. The input is a string to represent the month and an int to represent the day.

'''

# receive input and assign as variables
input_month = input()
input_day = input()

# establish valid months and days as a list
#list_month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
#if input_month not in list_months:
    #print('Invalid')

if input_month.lower == 'january' and input_day >= 1 and input_day <= 31:
    print('Winter')
