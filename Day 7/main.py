print("FAKE FAN FINDER")
print("----------------")

firstQuestion = input("I have a question for you, what is your favourite show?").lower()
if firstQuestion == "breaking bad":
  print("Oh really? lets see!")
  secondQuestion = input("What is the name of the main character?").lower()
  if secondQuestion == "walter white" or secondQuestion == "heisenberg":
    print("Okay, you are a real fan")
  elif secondQuestion == "jessie":
    print("Not quite the main character, but one of")
  else: 
    print("You're not a real fan!!")
elif firstQuestion == "better call saul":
  print(f"Oh really? lets see if it is {firstQuestion}")
  secondQuestion = input("What is the name of the main character?").lower()
  if secondQuestion == "saul goodman" or secondQuestion == "jimmy mcGill":
    print("Okay, you are a real fan")
  elif secondQuestion == "mike":
    print("Not quite the main character, but one of")
  else:
    print(f"You're not a real fan of {firstQuestion}!!")
else:
  print("I don't know that show")