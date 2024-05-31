import random
import time
import os

def text_color(color):
  if color == "red":
    return ("\033[31m")
  elif color == "blue":
    return ("\033[34m")
  elif color == "green":
    return ("\033[32m")
  elif color=="white":
    return ("\033[0m")
  elif color == "purple":
    return ("\033[35m")
  elif color=="yellow":
    return ("\033[33m")
  else:
    return ("\033[00m")

def six_and_eight():
  dice1 = roll_dice(6)
  dice2 = roll_dice(8)
  return dice1 * dice2

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
    title = f"{text_color('red')}Lee's Little Tool Box"
    option_one = f"{text_color('blue')}Option 1: Rolling a dice with the desired faces"
    option_two = f"{text_color('green')}Option 2: Generating character health"
    option_three = f"{text_color('purple')}Option 3: Create Character for game"
    option_four = f"{text_color('yellow')}Option 4: Create Character and battle"
    os.system("cls")
    print(f"{title: ^75}")
    time.sleep(0.5)
    print(f"{option_one: ^75}")
    time.sleep(0.5)
    print(f"{option_two: ^75}")
    time.sleep(0.5)
    print(f"{option_three: ^75}")
    time.sleep(0.5)
    print(f"{option_four: ^75}")
    print(f"{text_color('white')}")
    which_option = input("What option do you want? (1 / 2 / 3 / 4) ")
    
    if which_option == "1":
        sides = int(input("How many sides does the dice have? "))
        random_number = roll_dice(sides)
        print(random_number)
        
    elif which_option == "2":
        continue_choosing = "yes"
        while continue_choosing == "yes":
            character_name = input("Name your character: ")
            character_health = six_and_eight()
            print(f"Characters name: {character_name}")
            print(f"Characters Health: {character_health}hp")
            continue_choosing = input("Do you want to do another character? (yes/no): ").lower()
    
    elif which_option == "3":
        while True:
            print("Welcome to the character creation.. ")
            time.sleep(1)
            print("I am going to ask some questions, then we will generate the character..")
            time.sleep(1)
            print()
            
            name = str(character_name())
            race = character_race()
            health = character_health()
            strength = character_strength()

            if race != "human" and race != "elf" and race != "wizard" and race != "orc":
                print("Incorrect race, start again please.. ")
                continue
            else:
                print(f"""
                Character created!!

                Character Name: {name}
                Character Race: {race}
                Character Health: {health}
                Character Strength: {strength}

                Have fun with the game!!
                """)
            
            generate_another = input("Do you want to genreate another? (yes/no) ").lower()
            if generate_another == "yes":
                print("Let's generate another..")
                time.sleep(1)
                os.system("cls")
                continue
            else:
                print("Okay, we won't create anymore!")
                time.sleep(1)
                print(f"Have fun on your Journey, {3name}!")
                time.sleep(1)
                os.system("cls")
                break
        break
              
    elif which_option == "4":
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
            
            if player1_race not in valid_race:
                print("Incorrect race, start again please.. ")
                os.system("cls")
                continue
            
            print("Character 1 created!!") 
            time.sleep(1)
            os.system("cls")
            time.sleep(1)

            print("Now for player 2...")
            player2_name = character_name()
            player2_race = character_race()
            player2_health = character_health()
            player2_strength = character_strength()
            
            if player2_race not in valid_race:
                print("Incorrect race, start again please.. ")
                os.system("cls")
                continue
            
            print("Character 2 created!!") 
            time.sleep(1)
            os.system("cls")
            time.sleep(1)

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
            
            play_game = input("Are you ready to battle?! (yes/no) ")
            round = 0
            while play_game == "yes":
                os.system("cls")
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
            break
    else:
        print("Please choose the correct option..")
        
    continue_program = input("Do you want to continue and choose another from the main menu? (yes/no): ").lower()
    if continue_program != "yes":
        print("Okay, see ya!!")
        break












