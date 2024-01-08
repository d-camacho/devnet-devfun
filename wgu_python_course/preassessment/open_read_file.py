'''
Create a solution that accepts an input identifying the name of a text file, for example, "WordTextFile1.txt". Each text file contains three rows with one word per row. Using the open() function and write() and read() methods, interact with the input text file to write a new sentence string composed of the three existing words to the end of the file contents on a new line. Output the new file contents.

The solution output should be in the format

word1
word2
word3 
sentence
Sample Input/Output:
If the input is

WordTextFile1.txt
then the expected output is

cat
chases
dog
cat chases dog
'''

#open, write, and read text file (e.g., "WordTextFile1.txt") using open(), write(), read()
#solution accepts file input to insert sentence composed of file content into text file on a new line
#solution outputs the text file contents including the new sentence

#receive input file
file_name = input()

# read existing content of file
with open(file_name, 'r') as file:
    file_contents = file.read()
# extract words after reading and split using the .split method
words = file_contents.split()
for word in words:
    print(word)
sentence = ' '.join(words)
print(sentence)
    
file_name = input()

with open(file_name, 'r') as myfile:
    contents = myfile.read()
    words = contents.split()
    sentence = ' '.join(words)
print(words[0])
print(words[1])
print(words[2])
print(sentence)