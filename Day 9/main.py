print("Generation Identifier")
print("---------------------")
print()
birthDay = int(input("When were you born? "))
if birthDay <= 1946:
  print("You are a Traditionalist!")
elif birthDay >= 1947 and birthDay <= 1964:
  print("You are a Baby Boomer!")
elif birthDay >= 1965 and birthDay <= 1981:
  print("You are a Generation X!")
elif birthDay >= 1982 and birthDay <= 1995:
  print("You are a Millenial!")
elif birthDay >= 1996 and birthDay <= 2015:
  print("You are a Generation Z!")
else:
  print("You are either too old or too young to be on this list!")