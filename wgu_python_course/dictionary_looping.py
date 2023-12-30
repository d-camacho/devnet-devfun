'''
For loop: Printing a dictionary
Output each contact in contact_emails:
First, complete the for loop statement.
On the next line, provide the loop body with the appropriate print statement.
Sample output with inputs: 'Alf' 'alf1@hmail.com'
mike.filt@bmail.com is Mike Filt
s.reyn@email.com is Sue Reyn
narty042@nmail.com is Nate Arty
alf1@hmail.com is Alf

'''
contact_emails = {
    'Sue Reyn' : 's.reyn@email.com',
    'Mike Filt': 'mike.filt@bmail.com',
    'Nate Arty': 'narty042@nmail.com'
}

new_contact = input()
new_email = input()
contact_emails[new_contact] = new_email

for contact in contact_emails:
    print(f'{contact_emails[contact]} is {contact}') # extract key value then print key

# Using range() and len() to iterate over a sequence.
origins = [4, 8, 10]

for index in range(len(origins)):
    value = origins[index]  # Retrieve value of element in list.
    print(f'Element {index}: {value}')

# Using list.index() to find the index of each element.
origins = [4, 8, 10]

for value in origins:
    index = origins.index(value)  # Retrieve index of value in list
    print(f'Element {index}: {value}')   

'''
The enumerate() function retrieves both the index and corresponding element value at the same time, 
providing a cleaner and more readable solution.

'''
origins = [4, 8, 10]

for (index, value) in enumerate(origins):
    print(f'Element {index}: {value}')
