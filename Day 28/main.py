import random
import os
import time


def roll_dice(sides):
    return random.randint(1, sides)

def random_dice(amount):
  return random.randint(1, 6) * random.randint(1, 12) + int(amount)

def character_health():
  return random_dice(10)

def character_strength():
  return random_dice(12)

def health_update():
  print(f"""
  Character 1 Health: {player1_health}
  Character 2 Health: {player2_health}
  """)

def character_name():
  name = input("Name your character: ").lower()
  return name

def character_race():
  race = input("Choose your race (Human, Elf, Wiard, Orc): ").lower()
  return race

def damage():
    if player1_strength > player2_strength:
        damage = player1_strength - player2_strength + 1
    elif player1_strength == player2_strength:
        damage = 1
    else:
        damage = player2_strength - player1_strength + 1
    return damage


while True:
    print("Welcome to the character creation.. ")
    time.sleep(1)
    print("I am going to ask some questions, then we will generate the characters..")
    time.sleep(1)
    print()

    player1_name = character_name()
    player1_race = character_race()
    player1_health = character_health()
    player1_strength = character_strength()

    if player1_race != "human" and player1_race != "elf" and player1_race != "wizard" and player1_race != "orc":
        print("Incorrect race, start again please.. ")
        continue
    else:
      time.sleep(1)
      print("Character 1 created!!") 
      time.sleep(1)

    os.system("clear")
    time.sleep(1)

    print("Now for player 2...")
    player2_name = character_name()
    player2_race = character_race()
    player2_health = character_health()
    player2_strength = character_strength()

    if player2_race != "human" and player2_race != "elf" and player2_race != "wizard" and player2_race != "orc":
        print("Incorrect race, start again please.. ")
        continue
    else:
        time.sleep(1)
        print("Character 2 created!!") 
        time.sleep(1)
    os.system("clear")

    print(f"""
    Player stats!!

    Player 1:
      Character Name: {player1_name}
      Character Race: {player1_race}
      Character Health: {player1_health}
      Character Strength: {player1_strength}

    Player 2:
      Character Name: {player2_name}
      Character Race: {player2_race}
      Character Health: {player2_health}
      Character Strength: {player2_strength}
    """)  
    ready = input("Are you ready to battle?! (yes/no) ")
    if ready == "yes":
      break
    else:
      print("Tough, we are!!")
      time.sleep(1)
      break


round = 0
play_game = "yes"
while play_game == "yes":
    os.system("clear")
    round += 1
    damage_result = damage()
    damage_int = int(damage_result)
    player1_roll = roll_dice(6)
    player2_roll = roll_dice(6)

    if player1_roll > player2_roll:
        print(f"Player 1 wins round {round} with {player1_roll}")
        print(f"Damage dealt will be - {damage_int}")
        player2_health = player2_health - damage_int
        time.sleep(1)
      
    elif player1_roll == player2_roll:
        print("Draw! Roll again..")
        time.sleep(1)
        continue

    else:
        print(f"Player 2 wins round {round} with {player2_roll}")
        print(f"Damage dealt will be - {damage_int}")
        player1_health = player1_health - damage_int
        time.sleep(1)

    if player1_health <= 0:
      print("Player 1 has died. Player 2 wins.")
      health_update()  
      print(f"This took {round} rounds!! Good job.")
      break
      
    elif player2_health <= 0:
      print("Player 2 has died. Player 1 wins.")
      health_update()  
      print(f"This took {round} rounds!! Good job.")
      break
      
    else:
      print("Both players still standing, lets go again!!")
      health_update()  
      play_game = input("Are you ready for the next round? (yes/no) ")
      if play_game != "yes":
          print("Okay, we will stop then..")
          break
      
      
    