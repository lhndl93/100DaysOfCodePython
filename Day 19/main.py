start_loan = 1000
for i in range (10):
  start_loan += start_loan * 0.05
  print(f"Year {i + 1} is {round(start_loan, 2)}")
  print(f"This consists of Interest: {round(start_loan * 0.05, 2)}")
  print()