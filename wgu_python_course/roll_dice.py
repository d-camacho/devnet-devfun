'''
6.13 Additional practice: Dice statistics
The following is a sample programming lab activity; not all classes using a zyBook require students to fully complete this activity. No auto-checking is performed. Users planning to fully complete this program may consider first developing their code in a separate programming environment.

Analyzing dice rolls is a common example in understanding probability and statistics. The following program calculates the number of times the sum of two dice (randomly rolled) is equal to six or seven.
'''
'''
import random

num_sixes = 0
num_sevens = 0
num_rolls = int(input('Enter number of rolls:\n'))

if num_rolls >= 1:
    for i in range(num_rolls):
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        roll_total = die1 + die2

        #Count number of sixes and sevens
        if roll_total == 6:
            num_sixes = num_sixes + 1
        if roll_total == 7:
            num_sevens = num_sevens + 1
        print(f'Roll {i} is {roll_total} ({die1} + {die2})')

    print('\nDice roll statistics:')
    print('6s:', num_sixes)
    print('7s:', num_sevens)
else:
    print('Invalid number of rolls. Try again.')
'''
'''
Create a different version of the program that:

Calculates the number of times the sum of the randomly rolled dice equals each possible value from 2 to 12.
Repeatedly asks the user for the number of times to roll the dice, quitting only when the user-entered number is less than 1. 
Hint: Use a while loop that will execute as long as num_rolls is greater than 1.
Prints a histogram in which the total number of times the dice rolls equals each possible value is displayed 
by printing a character, such as *, that number of times. The following provides an example:

Dice roll histogram:

2s:  **
3s:  ****
4s:  ***
5s:  ********
6s:  *************
7s:  *****************
8s:  *************
9s:  *********
10s: **********
11s: *****
12s: **

'''

import random

user_roll = int(input('How many times do you want to roll? '))

values = {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
index = 0
val2 = 0
val3 = 0
val4 = 0 
val5 = 0
val6 = 0
val7 = 0
val8 = 0
val9 = 0
val10 = 0
val11 = 0
val12 = 0


while user_roll > 1:
    for i in range(user_roll):
        die_1 = random.randint(1,6)
        die_2 = random.randint(1,6)
        total_roll = die_1 + die_2             
        if total_roll == 2:
            val2 +=1
        if total_roll == 3:
            val3 +=1
        if total_roll == 4:
            val4 +=1
        if total_roll == 5:
            val5 +=1
        if total_roll == 6:
            val6 +=1
        if total_roll == 7:
            val7 +=1
        if total_roll == 8:
            val8 +=1
        if total_roll == 9:
            val9 +=1
        if total_roll == 10:
            val10 +=1
        if total_roll == 11:
            val11+=1
        if total_roll == 12:
            val12 +=1
    user_roll = int(input('Enter your next roll. Enter 0 to quit.'))
print('Dice roll histogram:')
print('2s: ', end=' ')
for num in range(val2):
    print('*', end=' ')
print()
print('3s: ', end=' ')
for num in range(val3):
    print('*', end=' ')
print()
print('4s: ', end=' ')
for num in range(val4):
    print('*', end=' ')
print()
print('5s: ', end=' ')
for num in range(val5):
    print('*', end=' ')
print()
print('6s: ', end=' ')
for num in range(val6):
    print('*', end=' ')
print()
print('7s: ', end=' ')
for num in range(val7):
    print('*', end=' ')
print()
print('8s: ', end=' ')
for num in range(val8):
    print('*', end=' ') 
print()          
print('9s: ', end=' ')
for num in range(val9):
    print('*', end=' ') 
print()
print('10s: ', end=' ')
for num in range(val10):
    print('*', end=' ') 
print()
print('11s: ', end=' ')
for num in range(val11):
    print('*', end=' ') 
print()
print('12s: ', end=' ')
for num in range(val12):
    print('*', end=' ')        