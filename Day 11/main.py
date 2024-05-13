leapYear = input("Is it a leap year? ").lower()

seconds = 60
minutes = 60
hours = 24
days = 366 if leapYear == "yes" else 365

  
if leapYear == "yes":
  print("There are", seconds * minutes * hours * days, "seconds in a leap year")
else:
  print("There are", seconds * minutes * hours * days, "seconds in a year")