'''
Create a solution that accepts one integer input representing the index value for any of the string elements in the following list:

frameworks = ["Django", "Flask", "CherryPy", "Bottle", "Web2Py", "TurboGears"]

Output the string element of the index value entered. The solution should be placed in a try block and implement an exception of "Error" if an incompatible integer input is provided.

The solution output should be in the format

frameworks_element
Sample Input/Output:
If the integer input is

2
then the expected output is

CherryPy
Alternatively, if the integer input is

7
then the expected output is

Error
'''

frameworks = ["Django", "Flask", "CherryPy", "Bottle", "Web2Py", "TurboGears"]

#use try block with exception "Error" when index value is not found in list
#solution accepts an integer input
#solution outputs the corresponding string value for the integer input

# determine if input is valid and process accordingly using try /block
try:
    index_value = int(input()) # receive index from user
    element = frameworks[index_value]
    print(element)
except IndexError:
    print('Error') # validates input if value is outside the range of list
except ValueError:
    print('Error') # validates input if value is non-integer


try:
    user_index = int(input())
    element = frameworks[user_index]
    print(element)
except:
    print('Error')