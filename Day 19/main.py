start_loan = 1000
for counter in range (10):
  start_loan += start_loan * 0.05
  print(f"Year {counter + 1} is {round(start_loan, 2)}")
  print(f"This consists of Interest: {round(start_loan * 0.05, 2)}")
  print()