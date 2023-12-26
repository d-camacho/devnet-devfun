'''
5.17 LAB: Golf scores
Golf scores record the number of strokes used to get the ball in the hole. 
The expected number of strokes varies from hole to hole and is called par (i.e. 3, 4, or 5). 
Each score's name is based on the actual strokes taken compared to par:

"Eagle": number of strokes is two less than par
"Birdie": number of strokes is one less than par
"Par": number of strokes equals par
"Bogey": number of strokes is one more than par
Given two integers that represent par and the number of strokes used, write a program that prints the appropriate score name. Print "Error" if par is not 3, 4, or 5.

Ex: If the input is:

4
3
the output is:
Birdie

'''
# receive input and assign as variables
par = int(input())
num_strokes = int(input())

# problem parameters
valid_par = [3,4,5]
# validate input to meet parameters
if par not in valid_par:
    print('Error')

# basic logic: compare par with strokes using if/elif then output scores
elif par - num_strokes >= 2:
    print('Eagle')
elif par - num_strokes == 1:
    print('Birdie')
elif par == num_strokes:
    print('Par')
elif par - num_strokes >= -1:
    print('Bogey')
