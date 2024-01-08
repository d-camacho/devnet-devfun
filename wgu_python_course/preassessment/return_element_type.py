'''
Create a solution that accepts an integer input representing the index value 
for any any of the five elements in the following list:

various_data_types = [516, 112.49, True, "meow", ("Western", "Governors", "University"), {"apple": 1, "pear": 5}]

Using the built-in function type() and getting its name by using the .name attribute, output data type (e.g., int”, “float”, “bool”, “str”) based on the input index value of the list element.

The solution output should be in the format

Element index_value: data_type
Sample Input/Output:
If the input is

4
then the expected output is

Element 4: tuple

'''
various_data_types = [516, 112.49, True, "meow", ("Western", "Governors", "University"), {"apple": 1, "pear": 5}]
element_index = int(input())

if 0 <= element_index < len(various_data_types):
    type_element = type(various_data_types[element_index]).__name__
    print(f'Element {element_index}: {type_element}')
else:
    print('Input is outside of range')


various_data_types = [516, 112.49, True, "meow", ("Western", "Governors", "University"), {"apple": 1, "pear": 5}]

#use built-in function type()
#get name by using the built-in attribute __name__
#solution accepts integer input representing list element index
#solution outputs data type of list element based on input index value

user_index = int(input())
element_type = type(various_data_types[user_index]).__name__
print(f'Element {user_index}: {element_type}')