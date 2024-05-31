def color(color, text):
  if color == "red":
    text = print(f"\033[31m{text}\033[00m")
  elif color == "blue":
    text = print(f"\033[34m{text}\033[00m")
  elif color == "green":
    text = print(f"\033[32m{text}\033[00m")
  return text

print("Testng this out")
color("red","This should be red")
print("Back to black?")
color("blue", "This should be blue??")
print("Back to black?")
color("green", "This should be green?")
print("Back to black?")

