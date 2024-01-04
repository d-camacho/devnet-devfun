'''
Task:
Create a solution that accepts an integer input representing any number of ounces. Output the converted total number of tons, pounds, and remaining ounces based on the input ounces value. There are 16 ounces in a pound and 2,000 pounds in a ton.

The solution output should be in the format

Tons: value_1
Pounds: value_2
Ounces: value_3
Sample Input/Output:
If the input is

32035
then the expected output is

Tons: 1
Pounds: 2
Ounces: 3

'''

#there are 16 ounces in a pound and 2000 pounds in a ton
#solution accepts an integer value representing any number of ounces
#solution outputs the converted tons, pounds, and ounces represented by the input value of ounces

user_ounces = int(input())

# determine weight in tons
weight_tons = user_ounces // (16 * 2000) # 16 ounces to a pound, 2000 pounds to a ton
# determine weight in pounds
weight_pounds = (user_ounces % (16 * 2000)) // 16 # remaining ounces from tons then converting them to pounds with // 16
# determine remaining ounces
weight_ounces = (user_ounces % (16 * 2000)) % 16 # remaining ounces after getting tons and pounds

print(f'Tons: {weight_tons}')
print(f'Pounds: {weight_pounds}')
print(f'Ounces: {weight_ounces}')

