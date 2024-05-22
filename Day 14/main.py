from getpass import getpass as input
print("ROCK PAPER SCISSORS")
print()
print("Select your move (R, P or S)")
print()

player1 = input("Player 1 > ").capitalize()  
print()
player2 = input("Player 2 > ").capitalize()

if player1 == "R":
  if player2 == "R":
    print("This is a tie!! Close though..")
  elif player2 == "P":
    print("PLAYER 2 WINS!! WOO! PAPER BEATS ROCK.")
  elif player2 == "S":
    print("PLAYER 1 WINS. ROCK BREAKS SCISSORS!!")
  else:
    print(f"Someone chose a wrong option.. Player1: {player1} - Player2: {player2}")
elif player1 == "P":
  if player2 == "R":
    print("PLAYER 1 WINS!! PAPER BEATS ROCK.")
  elif player2 == "P":
    print("This is a tie!! Close though..")
  elif player2 == "S":
    print("PLAYER 2 WINS!! SCISSORS CUTS PAPER!!")
  else:
    print(f"Someone chose a wrong option.. Player1: {player1} - Player2: {player2}")
elif player1 == "S":
  if player2 == "R":
    print("PLAYER 2 WINS!! ROCK BREAKS SCISSORS!!")
  elif player2 == "P":
    print("PLAYER 1 WINS!! SCISSORS CUTS PAPER!!")
  elif player2 == "S":
    print("This is a tie!! Close though..")
  else:
    print(f"Someone chose a wrong option.. Player1: {player1} - Player2: {player2}")
else:
  print(f"Someone chose a wrong option.. Player1: {player1} - Player2: {player2}")
  

