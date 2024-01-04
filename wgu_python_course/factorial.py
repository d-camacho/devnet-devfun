'''
Number factorial

'''
N = int(input())  # Read user-entered number
total = N
i = N - 1 # Initialize the loop variable

while i >= 1:
    total = total * i 
    i = i - 1 # Decrement i

print(total)