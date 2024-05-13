option = int(input("Do you want a full year (1) or days left (2)? "))

seconds = 60
minutes = 60
hours = 24

if option == 1:
  leapYear = input("Is it a leap year? ").lower()
  days = 366 if leapYear == "yes" and option == 1 else 365
  if leapYear == "yes":
    print("There are", seconds * minutes * hours * days, "seconds in a leap year")
  elif leapYear == "no":
    print("There are", seconds * minutes * hours * days, "seconds in a year")
  else:
    print("Invalid input")
elif option == 2:
  days = int(input("How many days are left? "))
  print("There are", seconds * minutes * hours * days, " seconds left this year.")
else: 
  print("Invalid input")
