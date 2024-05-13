option = input("Do you want a full year (1) or days left (2)? ")
leapYear = input("Is it a leap year? ").lower()

seconds = 60
minutes = 60
hours = 24
days = 366 if leapYear == "yes" else 365
daysLeft = days - int(option)


if option == 1:
  if leapYear == "yes":
    print("There are", seconds * minutes * hours * days, "seconds in a leap year")
  else:
    print("There are", seconds * minutes * hours * days, "seconds in a year")
elif option == 2:
  if leapYear == "yes":
    print("There are", seconds * minutes * hours * daysLeft, "seconds left in a leap year"")
  else:
    print("There are", seconds * minutes * hours * daysLeft, "seconds left in a year")
else:
  print("Invalid option")
    
