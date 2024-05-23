import random

myNumber = random.randint(1, 100)
attempts = 0
# print(myNumber)

print("Gussing number game!!!")

while True:
  playerGuess = int(input("What is you guess, huh?? "))
  attempts += 1
  if playerGuess < 0:
    print("Can't be a negative number..")
    exit()
  elif playerGuess < myNumber:
    print("oooooh too low buddy")
  elif playerGuess > myNumber:
    print("Ah no, that's too high!!")
  else:
    print(f"Woooohooo!! you guessed the correct number {myNumber}!")
    print(f"This took you {attempts} attempts")
    exit()