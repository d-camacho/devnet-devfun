'''
Task:
Create a solution that accepts an integer input to compare against the following list:

predef_list = [4, -27, 15, 33, -10]

Output a Boolean value indicating whether the input value is greater than the maximum value from predef_list

The solution output should be in the format

Greater Than Max? Boolean_value
Sample Input/Output:
If the input is

20
then the expected output is

Greater Than Max? False
'''

predef_list = [4, -27, 15, 33, -10]

#solution accepts an integer input
#solution outputs Boolean value indicating if integer input is greater than the maximum value when compared to predef_list

# receive input to compare 
user_input = int(input())

# determine max from list
i = 0
max = 0
for i in range(len(predef_list)):
    if predef_list[i] > max:
        max = predef_list[i]
        
print('Greater Than Max?', end=' ')
if user_input > max:
    print('True')
else:
    print('False')