'''
CHALLENGE ACTIVITY
6.3.3: While loop: Insect growth.
Given positive integer num_insects, write a while loop that prints, then doubles, num_insects each iteration. 
Print values ≤ 100. Follow each number with a space.

Sample output with input: 8
8 16 32 64

'''
# input must be positive value
num_insects = int(input()) 

# process to double num_insects
while num_insects <= 100:
    print(num_insects, end=' ') # output with space in between and not starting a new line
    num_insects = num_insects * 2

