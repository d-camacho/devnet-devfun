'''
Create a solution that accepts an integer input. Import the built-in module math and use its factorial() method to calculate the factorial of the integer input. Output the value of the factorial, as well as a Boolean value identifying whether the factorial output is greater than 100.

The solution output should be in the format

factorial_value
Boolean_value
Sample Input/Output:
If the input is

10
then the expected output is

3628800
True
Alternatively, if the input is

3
then the expected output is

6
False
'''
#import math module and call factorial()
#solution accepts integer input
#solution outputs the factorial of the integer input 
#solution outputs Boolean identification of whether the factorial is >100

import math

user_input = int(input())

final_value = math.factorial(user_input) # determine value using factorial method
greater_than_100 = final_value > 100 # determine if final_value is greater or less than 100 (output is boolean)

# output
print(final_value)
print(greater_than_100)

import math
num_to_convert = int(input())

factorial_value = math.factorial(num_to_convert)
print(factorial_value)
print(factorial_value > 100)