'''
6.15 LAB: Password modifier
Many user-created passwords are simple and easy to guess. Write a program that takes a simple password and makes it stronger by replacing characters using the key below, and by appending "!" to the end of the input string.

i becomes 1
a becomes @
m becomes M
B becomes 8
s becomes $
Ex: If the input is:

mypassword
the output is:

Myp@$$word!
Hint: Python strings are immutable, but support string concatenation. Store and build the stronger password in the given password variable.

'''
word = input()
password = ''

code = {
    'i':'1',
    'a':'@',
    'm':'M',
    'B':'8',
    's':'$'}

for char in word:
    password += code.get(char, char) # use the get method to match every character of word to the list and assign it to password
password = password + '!'
print(password)