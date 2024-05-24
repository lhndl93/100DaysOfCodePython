import random

# generating a random number
myNumber = random.randint(1, 1000000)
attempts = 0
# print(myNumber) # debugging

print("Gussing number game!!!")

while True:
    # asking player for there guess
    playerGuess = int(input("What is you guess, huh?? "))
    attempts += 1
    # checking if it is a negative number
    if playerGuess < 0:
        print("Can't be a negative number..")
        exit()
    # checking if the number is too low
    elif playerGuess < myNumber:
        print("oooooh too low buddy")
    # checking is number it too high
    elif playerGuess > myNumber:
        print("Ah no, that's too high!!")
    # if number is correct, prints a well done
    else:
        print(f"Woooohooo!! you guessed the correct number {myNumber}!")
        print(f"This took you {attempts} attempts")
        exit()