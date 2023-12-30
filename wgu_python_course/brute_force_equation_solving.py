'''
6.16 LAB: Brute force equation solver
Numerous engineering and scientific applications require finding solutions to a set of equations. Ex: 8x + 7y = 38 and 3x - 5y = -1 have a solution x = 3, y = 2. Given integer coefficients of two linear equations with variables x and y, use brute force to find an integer solution for x and y in the range -10 to 10.

Ex: If the input is:

8
7
38
3
-5
-1
Then the output is:

x = 3 , y = 2
Use this brute force approach:

For every value of x from -10 to 10
   For every value of y from -10 to 10
      Check if the current x and y satisfy both equations. If so, output the solution, and finish.
Ex: If no solution is found, output:
    There is no solution
'''

''' Read in first equation, ax + by = c '''
a = int(input())
b = int(input())
c = int(input())


''' Read in second equation, dx + ey = f '''
d = int(input())
e = int(input())
f = int(input())

# create empty list first to store possible values (eventhough Lab says you should assume there's only one solution
match_x = 0
match_y = 0
# loop through all possible values of x and y and see if it meets both formulas
for x in range(-10, 11):
    for y in range(-10, 11):
        if ((a * x) + (b * y) == c) and ((d * x) + (e * y) == f) == True: 
            match_x = x
            match_y = y
            continue
if match_x == 0 and match_y == 0:
    print('There is no solution')
else:  
    print(f'x = {match_x} , y = {match_y}')