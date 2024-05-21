testName = input("What is the name of the test? ")
maximumScore =float(input("What is the maximum score you could get? "))
scoreReceived = float(input("What score did you get? "))
percentage = round(scoreReceived / maximumScore * 100, 2)

if percentage >= 90:
  print(f"You got an A+ with {percentage}%")
elif percentage >= 80:
  print(f"You got an A  with {percentage}%")
elif percentage >= 70:
  print(f"You got a B with {percentage}%")
elif percentage >= 60:
  print(f"You got a C with {percentage}%")
elif percentage >= 50:
  print(f"You got a D with {percentage}%")
else:
  print(f"You got a U with {percentage}%, terrible!")
