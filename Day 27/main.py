import random
import os
import time

def random_dice(amount):
  return random.randint(1, 6) * random.randint(1, 12) + int(amount)


def character_health():
  return random_dice(10)

def character_strength():
  return random_dice(12)

def character_name():
  name = input("Name your character: ").lower()
  return name

def character_race():
  race = input("Choose your race (Human, Elf, Wiard, Orc): ").lower()
  return race

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
    os.system("clear")
    print(f"Have fun on your Journey, {name}!")
    break
  
  
  
  





  


