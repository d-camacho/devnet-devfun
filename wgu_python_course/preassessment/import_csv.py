'''
Create a solution that accepts an input identifying the name of a CSV file, for example, "input1.csv". Each file contains two rows of comma-separated values. 
Import the built-in module csv and use its open() function and reader() method to create a dictionary of key:value pairs for each row of comma-separated values in the specified file. 
Output the file contents as two dictionaries.

The solution output should be in the format

{'key': 'value', 'key': 'value', 'key': 'value'}
{'key': 'value', 'key': 'value', 'key': 'value'}
Sample Input/Output:
If the input is

input1.csv
then the expected output is

{'a': '100', 'b': '200', 'c': '300'}
{'bananas': '1.85', 'steak': '19.99', 'cookies': '4.52'}
Alternatively, if the input is

input2.csv
then the expected output is

{'d': '400', 'e': '500', 'f': '600'}
{'celery': '2.81', 'milk': '4.34', 'bread': '5.63'}
'''

#import csv module and call open(), reader()
#solution accepts input identifying name of CSV file (i.e., "input1.csv")
#solution outputs each row of CSV file contents as a dictionary of elements

import csv

file_name = input("Enter the name of the CSV file: ")

with open(file_name, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    for row in csv_reader:
        # Create a dictionary using pairs of alternating elements in the row
        row_dict = {row[i].strip(): row[i + 1].strip() for i in range(0, len(row), 2)}
        print(row_dict)




# always break stuff down.
'''
{ key:value for key, value in thing} is a dict comprehension. It is a more complicated brother to list comprehensions. 
You are better off starting out to use a for loop as they are pretty much the same and easier to read.
'''
output = {}

for i in range(0, len(row), 2):
    key = row[i].strip()
    value = row[i + 1].strip()
    output[key] = value
# or

output = {}

for i in range(0, len(row), 2):
    output[row[i].strip()]  = row[i + 1].strip()

# So really it is as much about readability as anything else. I'd probably chose the last example as the sweet spot in this example.
    
