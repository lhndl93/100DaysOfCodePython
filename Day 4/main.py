print("""Welcome to your adventure simulator. I am going 
  to ask you a bunch of questions and then create an epic 
  story with you as the star!""")

print()

colorRed = "\033[31m"
colorEnd = "\033[0m"
yourName = input("What is your charatcers name? ")
yourAge = input("What is your characters age? ")
yourGender = input("What is your characters gender? ")
location = input("Where is your character from? ")
yourSuperpower = input("What is your characters superpower? ")
faveFood = input("What is your characters favourite food? ")
yourEnemy = input("Who is your characters enemy? ")

print(
    f"""Hello {colorRed}{yourName}{colorEnd} You are {colorRed}{yourAge}{colorEnd} and a {colorRed}{yourGender}{colorEnd}. Your ability to 
    {colorRed}{yourSuperpower}{colorEnd} will  make sure you  never have to look at {colorRed}{yourEnemy}{colorEnd} again. 
    Go eat {colorRed}{faveFood}{colorEnd} as you walk down the streets of 
    {colorRed}{location}{colorEnd} and use {colorRed}{yourSuperpower}{colorEnd} for good and not evil!"""
)
