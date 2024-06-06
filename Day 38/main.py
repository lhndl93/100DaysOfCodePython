title = "LET'S RAINBOW THIS SHIZZZZ"
print(f"{title:^50}")
print("")
text = input("Please enter a string.. ")


def change(color):
  if color == "b":
    print("\033[34m", end="")
  elif color == "g":
    print("\033[32m", end="")
  elif color == "p":
    print("\033[35m", end="")
  elif color == "y":
    print("\033[33m", end="")
  elif color == " ":
    print("\033[00m", end="")


for letters in text:
  change(letters.lower())
  print(letters, end ="")