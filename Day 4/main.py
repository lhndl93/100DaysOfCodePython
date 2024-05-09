print("""Welcome to your adventure simulator. I am going 
  to ask you a bunch of questions and then create an epic 
  story with you as the star!""")

print()

yourName = input("What is your charatcers name? ")
yourAge = input("What is your characters age? ")
yourGender = input("What is your characters gender? ")
location = input("Where is your character from? ")
yourSuperpower = input("What is your characters superpower? ")
faveFood = input("What is your characters favourite food? ")
yourEnemy = input("Who is your characters enemy? ")

print(
    f"""Hello \033[31m{yourName}\033[0m! You are \033[31m{yourAge}\033[0m! and a \033[31m{yourGender}\033[0m!. Your ability to 
    \033[31m{yourSuperpower}\033[0m! will  make sure you  never have to look at \033[31m{yourEnemy}\033[0m! again. 
    Go eat \033[31m{faveFood}\033[0m! as you walk down the streets of 
    \033[31m{location}\033[0m! and use \033[31m{yourSuperpower}\033[0m for good and not evil!"""
)
