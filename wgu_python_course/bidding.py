'''
Simple while loop program that generates bids as long as user input is yes (y)
'''

import random # random function
random.seed(5) # sets a seed to verify output on ZyLearning. program will run without this.

keep_bidding = 'y'
next_bid = 0

while keep_bidding != 'n':
   next_bid = next_bid + random.randint(1, 10)
   print(f'I\'ll bid ${next_bid}!')
   print('Continue bidding? (y/n)', end=' ')
   keep_bidding = input()