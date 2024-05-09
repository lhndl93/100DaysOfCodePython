mealType = input("1 = Breakfast, 2 = Lunch, 3 = Dinner: ")

if mealType == "1":
  print("Lets make a breakfast recipe")
  cerealType = input("Give me a type of cereal: ")
  milkType = input("Give me a type of milk: ")
  print("Lets have a bowl of ", cerealType, "with ", milkType, " milk.")
elif mealType == "2":
  print("Lets make a lunch recipe")
  meatType = input("Give me a type of meat: ")
  vegetableType = input("Give me a type of vegetable: ")
  print("Lets have ,", meatType, " with some ", vegetableType, 
        " on the side.")
elif mealType == "3":
  print("Lets make a dinner recipe")
  ingredientType1 = input("First ingredient? ")
  ingredientType2 = input("Second ingredient? ")
  ingredientType3 = input("Third ingredient? ")
  print("Lets put the", ingredientType1, ingredientType2, 
        "and the", ingredientType3, "together.")



  
  # foodType = input("Give me a type of food: ")
  # plantType = input("Give me a type of plant: ")
  # cookingMethod = input("Give me a cookng method ")
  # burnedFood = input("Give me a descriptive word for burning food ")
  # householdItem = input("Give me a household item ")

  # print(cookingMethod, foodType, "with", burnedFood, plantType,
  # "on a bed of", householdItem)