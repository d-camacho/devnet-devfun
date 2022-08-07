import random

# player input against random computer's random choice #
player = input("Let's play rock, paper, scissors. Your turn: ")
generated = random.choice (["rock", "paper", "scissors"])
print("I picked {}".format(generated))

# to determine who wins #
if player == "rock":   
    if generated == "rock":
        print("It's a tie! Lets go again!")
    elif generated == "paper":
        print("Paper beats rock. I win!")
    elif generated == "scissors":
        print("Ouch, you win!")

if player == "paper":
    if generated == "paper":
        print("Its a tie. Lets play again!")
    elif generated == "rock":
        print("Dangit...you win!")
    elif generated == "scissors":
        print("I win this round!")

if player == "scissors":
    if generated == "rock":
        print("Hard rock dulls a pair of scissors. I win!")
    if generated == "paper":
        print("Cut my life into pieces. I lost this one!")
    if generated == "scissors":
        print("It's a tie! Let's play again!")