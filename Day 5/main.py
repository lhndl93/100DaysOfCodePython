print("Marvel Character Guesser!")

RED = "\033[31m"
END = "\033[0m"

spider_man = input("Do you like 'hanging around'? ").lower()
if spider_man == "yes":
    print(f"{RED}Hello Spiderman!!{END}")
else:
    print("Let's try again then!")
    hulk = input("Do you like the color green? ").lower()
    if hulk == "yes":
        print(f"{RED}Hello Hulk!!{END}")
    else:
        print("Let's try it again!")
        iron_man = input("Do you like your tech? ").lower()
        if iron_man == "yes":
            print(f"{RED}Hello Ironman!!{END}")
        else:
            print("Let's try it again!")
            black_widow = input("Do you like to fight? ").lower()
            if black_widow == "yes":
                print(f"{RED}Hello Black Widow!!{END}")
            else:
                print(f"{RED}You must be Captain America then...{END}")
