import random

print("""      
      Lee's little tool box - 
      Option 1: Rolling a dice with the desired faces
      Option 2: Generating character health
           
      """)

def roll_dice(sides):
    return random.randint(1, sides)

def six_and_eight():
  dice1 = roll_dice(6)
  dice2 = roll_dice(8)
  return dice1 * dice2

while True:
    which_option = input("What option do you want? (1 / 2) ")
    
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
            
    else:
        print("Please choose the correct option..")
        
    continue_program = input("Do you want to continue and choose another from the main menu? (yes/no): ").lower()
    if continue_program != "yes":
        print("Okay, see ya!!")
        break

