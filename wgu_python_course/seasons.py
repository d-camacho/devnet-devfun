'''
5.15 LAB: Seasons
Write a program that takes a date as input and outputs the date's season in the northern hemisphere. The input is a string to represent the month and an int to represent the day.

The dates for each season in the northern hemisphere are:
Spring: March 20 - June 20
Summer: June 21 - September 21
Autumn: September 22 - December 20
Winter: December 21 - March 19

Ex: If the input is:

April
11
the output is:

Spring
In addition, check if the string and int are valid (an actual month and day).

Ex: If the input is:

Blue
65
the output is:

Invalid 

'''

# receive input and assign as variables
input_month = input()
input_day = int(input())

# determine if input is winter
if input_month.lower() == 'december' and (input_day >= 21 and input_day <= 31):
    print('Winter')
elif input_month.lower() == 'january' and (input_day >= 1 and input_day <= 31):
    print('Winter')
elif input_month.lower() == 'february' and (input_day >= 1 and input_day <= 29):
    print('Winter')
elif input_month.lower() == 'march' and (input_day >= 1 and input_day <= 19):
    print('Winter')

# determine if input is Spring
elif input_month.lower() == 'march' and (input_day >= 20 and input_day <= 31):
    print('Spring')
elif input_month.lower() == 'april' and (input_day >= 1 and input_day <= 30):
    print('Spring')
elif input_month.lower() == 'may' and (input_day >= 1 and input_day <= 31):
    print('Spring')
elif input_month.lower() == 'june' and (input_day >= 1 and input_day <= 20):
    print('Spring')

# determine if input is Summer
elif input_month.lower() == 'june' and (input_day >= 21 and input_day <= 30):
    print('Summer')
elif input_month.lower() == 'july' and (input_day >= 1 and input_day <= 31):
    print('Summer') 
elif input_month.lower() == 'august' and (input_day >= 1 and input_day <= 31):
    print('Summer') 
elif input_month.lower == 'september' and (input_day >= 1 and input_day <= 21):
    print('Summer')

# determine if input is Autumn
elif input_month.lower() == 'september' and (input_day >= 22 and input_day <= 30):
    print('Autumn')  
elif input_month.lower() == 'october' and (input_day >= 22 and input_day <= 31):
    print('Autumn')
elif input_month.lower() == 'november' and (input_day >= 1 and input_day <= 30):
    print('Autumn') 
elif input_month.lower() == 'december' and (input_day >= 1 and input_day <= 20):
    print('Autumn')   

else:
    print('Invalid')


