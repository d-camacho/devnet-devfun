'''
CHALLENGE ACTIVITY
6.8.3: Nested loops: Print seats.
Given num_rows and num_cols, print a list of all seats in a theater. Rows are numbered, columns lettered, as in 1A or 3E. Print a space after each seat.

Sample output with inputs: 2 3
1A 1B 1C 2A 2B 2C 

'''

num_rows = int(input())
num_cols = int(input())

# Note 1: You will need to declare more variables
# Note 2: Place end=' ' at the end of your print statement to separate seats by spaces

# assign numbers to alphabet
int_to_letters = {1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F'} # stopped at F for the sake of time

#solve using for loops
for row in range(1, num_rows + 1): # range has to start with 1 and not 0
    for col in range(1, num_cols + 1): # range has to start with 1 and not 0
        print(f'{row}{int_to_letters[col]}', end= ' ')

# solve using while loops
row = 1
while row <= num_rows:
    col = 1
    while col <= num_cols:
        print(f'{row}{int_to_letters[col]}', end = ' ')
        col += 1
    row += 1
    
