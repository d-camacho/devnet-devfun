'''
CHALLENGE ACTIVITY
6.10.2: Simon says.
"Simon Says" is a memory game where "Simon" outputs a sequence of 10 characters (R, G, B, Y) 
and the user must repeat the sequence. Create a for loop that compares each character of the two strings. 
For each matching character, add one point to user_score. Upon a mismatch, end the loop.

Sample output with inputs: 'RRGBRYYBGY' 'RRGBBRYBGY'
User score: 4

'''
simon_sequence = input()
user_sequence = input()
user_score = 0

# solve by comparing both characters simultaneously using zip to combine both string sequences
for simon_char, user_char in zip(simon_sequence, user_sequence):
    if simon_char == user_char:
        user_score += 1
    else:
        break  # End the loop upon a mismatch
print("User score:", user_score)

# solve using nested for loops and compring using indeces
min_length = min(len(simon_sequence), len(user_sequence)) # Make sure the loop doesn't go beyond the length of the shorter sequence
for i in range(min_length):
    simon_char = simon_sequence[i]
    user_char = user_sequence[i]

    if simon_char == user_char:
        user_score += 1
    else:
        break  # End the loop upon a mismatch
print("User score:", user_score)


       
    

#print('User score:', user_score)