print("AFFIRMATION GENERATOR")
print("---------------------")
print()

yourName = input("What is your name? ")
print("Hey! Nice to meet you", yourName)
dayOfTheWeeks = input("What day of the week is it? ").lower()
workingDay = input("Are you working today? ").lower()
if dayOfTheWeeks == "monday":
  if workingDay == "yes":
    print("Hey, it's Monday! You got this!")
  else:
    print("You're not working anyway, chill out buddy")
elif dayOfTheWeeks == "tuesday":
  if workingDay == "yes":
    print("Hey, it's Tuesday! Almost half way through the week!!")
  else:
    print("You're not working anyway, chill out buddy")
elif dayOfTheWeeks == "wednesday":
  if workingDay == "yes":
    print("Hey, it's Wednesday! Half way through the week! now!")
  else:
    print("You're not working anyway, chill out buddy")
elif dayOfTheWeeks == "thursday":
  if workingDay == "yes":
    print("Hey, it's Thursday! Almost Friday!")
  else:
    print("You're not working anyway, chill out buddy")
elif dayOfTheWeeks == "friday":
  if workingDay == "yes":
    print("Hey, it's Friday! Time to relax after today!!")
  else:
    print("You're not working anyway, chill out buddy")
else:
  print("You're off work now, so chillllll!")