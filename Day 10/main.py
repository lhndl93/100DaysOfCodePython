myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
tipAmount = int(input("What percentage of tip would you like to leave? "))

myBill += myBill * (tipAmount / 100)
splitAnswer = myBill / numberOfPeople

print("You all owe", round(splitAnswer, 2))