print("ANIMAL SOUNDS")
print()

def animal():
    exit_choice = "no"
    while exit_choice == "no":
        animal_choice = input("What animal do you want? (cow/dog) ").lower()
        if animal_choice == "cow":
            print("MOOOOOOOOOOO")
        elif animal_choice == "dog":
            print("WOOF")
        else:
            print("Choose a cow or a dog please..")  
        exit_choice = input("Do you want to exit? (yes/no) ").lower()

animal()