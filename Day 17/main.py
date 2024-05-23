from getpass import getpass as input
print("ROCK PAPER SCISSORS")
print()
print("Select your move (R, P or S)")
print()


player1Score = 0
player2Score = 0


def getPlayerInput(playerNum):
  return input(f"Player {playerNum} > ").capitalize()  

while True:

  player1 = getPlayerInput(1) 
  player2 = getPlayerInput(2)

  if player1 == "R":
    if player2 == "R":
      print("This is a tie!! Close though..")
    elif player2 == "P":
      print("PLAYER 2 WINS!! WOO! PAPER BEATS ROCK.")
      player2Score += 1
    elif player2 == "S":
      print("PLAYER 1 WINS. ROCK BREAKS SCISSORS!!")
      player1Score += 1
    else:
      print(f"Someone chose a wrong option.. Player1: {player1} - Player2: {player2}")

  elif player1 == "P":
    if player2 == "R":
      print("PLAYER 1 WINS!! PAPER BEATS ROCK.")
      player1Score += 1
    elif player2 == "P":
      print("This is a tie!! Close though..")
    elif player2 == "S":
      print("PLAYER 2 WINS!! SCISSORS CUTS PAPER!!")
      player2Score += 1
    else:
      print(f"Someone chose a wrong option.. Player1: {player1} - Player2: {player2}")

  elif player1 == "S":
    if player2 == "R":
      print("PLAYER 2 WINS!! ROCK BREAKS SCISSORS!!")
      player2Score += 1
    elif player2 == "P":
      print("PLAYER 1 WINS!! SCISSORS CUTS PAPER!!")
      player1Score += 1
    elif player2 == "S":
      print("This is a tie!! Close though..")
    else:
      print(f"Someone chose a wrong option.. Player1: {player1} - Player2: {player2}")

  else:
    print(f"Someone chose a wrong option.. Player1: {player1} - Player2: {player2}")


  print(f"Scores -> Player 1: {player1Score}, Player 2: {player2Score}")
  print()

  if player1Score == 3:
    print("PLAYER ONE WINS, THEY GOT 3!!")
    exit()
  elif player2Score == 3:
    print("PAYER 2 WINS, THEY GOT 3 POINTS!!!")
    exit()
  else:
    continue

