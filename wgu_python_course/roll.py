'''
This is more efficient and cleaner by using a list to store the counts for each total roll, 
and then use a loop to print the histogram

'''
import random

user_roll = int(input('How many times do you want to roll? '))

# Initialize a list to store counts for each total roll
counts = [0] * 11

while user_roll > 0:
    for i in range(user_roll):
        die_1 = random.randint(1, 6)
        die_2 = random.randint(1, 6)
        total_roll = die_1 + die_2
        # Increment the count for the corresponding total roll
        counts[total_roll - 2] += 1

    user_roll = int(input('Enter your next roll. Enter 0 to quit.'))

print('Dice roll histogram:')
for i, count in enumerate(counts, start=2):
    print(f'{i}s: {"*" * count}')
