import random

print("Rolling a dice, with a twist!!")
print()

sides = int(input("How many sides does the dice have? "))
play_game = "yes"

def roll_dice(sides):
    print(random.randint(1, sides))
    
while play_game == "yes":
    roll_dice(sides)
    play_game = input("Play again? ").lower()

print("Oh okay, see ya later!")