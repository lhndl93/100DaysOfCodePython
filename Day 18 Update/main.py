import random

myNumber = random.randint(1, 100)
attempts = 0
# print(myNumber)

print("Gussing number game!!!")

name = input("What is your name? ")

def playerGuess():
  guess = int(input(f"What is your guess {name}, huh?? "))
  return guess

while True:
  guess = playerGuess()
  attempts += 1
  if guess < 0:
    print("Can't be a negative number..")
    exit()
  elif guess < myNumber:
    print("oooooh too low buddy")
  elif guess > myNumber:
    print("Ah no, that's too high!!")
  else:
    print(f"Woooohooo!! you guessed the correct number {myNumber}!")
    print(f"This took you {attempts} attempts")
    exit()