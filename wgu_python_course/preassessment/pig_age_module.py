'''
Create a solution that accepts an integer input representing the age of a pig. Import the existing module pigAge and use its pre-built pigAge_converter() function to calculate the human equivalent age of a pig. A year in a pig's life is equivalent to five years in a human's life. Output the human-equivalent age of the pig.

The solution output should be in the format

input_pig_age is converted_pig_age in human years
Sample Input/Output:
If the input is

8
then the expected output is

8 is 40 in human years
'''

#import pigAge module and call pigAge_converter()
#one pig year is equivalent to five human years
#solution accepts integer input representing a pig's age
#solution outputs the human equivalent age for a pig (i.e. "8 is 40 in human years")

import pigAge
pig_age = int(input())

converted_age = pigAge.pigAge_converter(pig_age)
print(f'{pig_age} is {converted_age} in human years')