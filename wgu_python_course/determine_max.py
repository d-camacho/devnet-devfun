'''
Simple program to determine highest value given a set of numbers until a sentinel is entered.
In this case, the sentinel is 0 or any negative numbers.

'''

entered_value = int(input())

maximum_number = entered_value

while entered_value > 0:
    if entered_value > maximum_number:
        maximum_number = entered_value
    entered_value = int(input())

print('Max value:', maximum_number, end='')