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

def character_magic():
  return random_dice(15)

def character_range():
  return random_dice(13)

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


valid_race = ["human", "elf", "wizard", "orc"]
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
    
    # if player1_race == "wizard":
    #   player1_magic = character_magic()
    # elif player1_race == "elf":
    #   player1_range = character_range()
    # else:
    #   player1_strength = character_strength()

    if player1_race not in valid_race:
        print("Incorrect race, start again please.. ")
        os.system("clear")
        continue
    
    print("Character 1 created!!") 
    time.sleep(1)
    os.system("clear")
    time.sleep(1)

    print("Now for player 2...")
    player2_name = character_name()
    player2_race = character_race()
    player2_health = character_health()
    player2_strength = character_strength()
    
    # if player2_race == "wizard":
    #   player2_magic = character_magic()
    # elif player2_race == "elf":
    #   player2_range = character_range()
    # else:
    #   player2_strength = character_strength()

    if player2_race not in valid_race:
        print("Incorrect race, start again please.. ")
        os.system("clear")
        continue
    
    print("Character 2 created!!") 
    time.sleep(1)
    os.system("clear")
    time.sleep(1)

    
    # if player1_race == "wizard":
    #   print_stats1 = f"Character Magic: {player1_magic}"
    # elif player1_race == "elf":
    #   print_stats1 = f"Character Range: {player1_range}"
    # else:
    #   print_stats1 = f"Character Strength: {player1_strength}"

    # if player2_race == "wizard":
    #   print_stats2 = f"Character Magic: {player2_magic}"
    # elif player2_race == "elf":
    #   print_stats2 = f"Character Range: {player2_range}"
    # else:
    #   print_stats2 = f"Character Strength: {player2_strength}"

    print_stats1 = f"Character Strength: {player1_strength}"
    print_stats2 = f"Character Strength: {player2_strength}"
    print(f"""
    Player stats!!

    Player 1:
      Character Name: {player1_name}
      Character Race: {player1_race}
      Character Health: {player1_health}
      {print_stats1}

    Player 2:
      Character Name: {player2_name}
      Character Race: {player2_race}
      Character Health: {player2_health}
      {print_stats2}
    """)  
    
    ready = input("Are you ready to battle?! (yes/no) ")
    if ready == "yes":
      time.sleep(1)
      print("Okay, lets go!!")
      time.sleep(1)
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
        time.sleep(1)
        print(f"Damage dealt will be - {damage_int}")
        player2_health = player2_health - damage_int
        time.sleep(1)
      
    elif player1_roll == player2_roll:
        print("Draw! Roll again..")
        time.sleep(1)
        continue

    else:
        print(f"Player 2 wins round {round} with {player2_roll}")
        time.sleep(1)
        print(f"Damage dealt will be - {damage_int}")
        player1_health = player1_health - damage_int
        time.sleep(1)

    if player1_health <= 0:
      print("Player 1 has died. Player 2 wins.")
      time.sleep(1)
      health_update()  
      print(f"This took {round} rounds!! Good job.")
      break
      
    elif player2_health <= 0:
      print("Player 2 has died. Player 1 wins.")
      time.sleep(1)
      health_update()  
      print(f"This took {round} rounds!! Good job.")
      break
      
    else:
      print("Both players still standing, lets go again!!")
      time.sleep(1)
      health_update()  
      play_game = input("Are you ready for the next round? (yes/no) ")
      if play_game != "yes":
          print("Okay, we will stop then..")
          break
      
      
    