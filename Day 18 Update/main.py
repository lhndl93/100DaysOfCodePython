import random

my_number = random.randint(1, 100)
attempts = 0
# print(my_number)  # Uncomment for debugging

print("Guessing number game!!!")

name = input("What is your name? ")

def player_guess():
    guess = int(input(f"What is your guess {name}, huh?? "))
    return guess

while True:
    guess = player_guess()
    attempts += 1
    if guess < 0:
        print("Can't be a negative number..")
        exit()
    elif guess < my_number:
        print("oooooh too low buddy")
    elif guess > my_number:
        print("Ah no, that's too high!!")
    else:
        print(f"Woooohooo!! you guessed the correct number {my_number}!")
        print(f"This took you {attempts} attempts")
        exit()
