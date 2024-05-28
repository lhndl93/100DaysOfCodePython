import random
import time
import os

def random_dice(amount):
  return random.randint(1, 6) * random.randint(1, 12) + int(amount)

def character_health():
  return random_dice(10)

def character_strength():
  return random_dice(12)

def character_name():
  name = input("Name your character: ")
  return name

def character_race():
  race = input("Choose your race (Human, Elf, Wiard, Orc): ").lower()
  return race

def roll_dice(sides):
    return random.randint(1, sides)

def six_and_eight():
  dice1 = roll_dice(6)
  dice2 = roll_dice(8)
  return dice1 * dice2

while True:
    
    print("""      
      Lee's little tool box - 
      Option 1: Rolling a dice with the desired faces
      Option 2: Generating character health
      Option 3: Create Character for game
           
      """)
    
    which_option = input("What option do you want? (1 / 2 / 3) ")
    
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
            
            name = character_name()
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
                os.system("clear")
                continue
            else:
                print("Okay, we won't create anymore!")
                time.sleep(1)
                print(f"Have fun on your Journey, {name}!")
                time.sleep(1)
                os.system("clear")
                break
    else:
        print("Please choose the correct option..")
        
    continue_program = input("Do you want to continue and choose another from the main menu? (yes/no): ").lower()
    if continue_program != "yes":
        print("Okay, see ya!!")
        break

