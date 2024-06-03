import os

todo_list = []

def print_list():
  for item in todo_list:
    print(item)

def print_menu():
  title = "To Do List Manager"
  options = {
      '1': '1. View List',
      '2': '2. Add to List',
      '3': '3. Edit Item on List',
      '4': '4. Remove Item on List',
      '5': '5. DELETE WHOLE LIST'
  }
  # option_one = "1. View List"
  # option_two = "2. Add to List"
  # option_three = "3. Edit Item on List"
  # option_four = "4. Remove Item on List"
  # option_five = "5. DELETE WHOLE LIST"
  print(f"{title: ^35}")
  print("")
  print(f"{options['1']: ^35}")
  print(f"{options['2']: ^35}")
  print(f"{options['3']: ^35}")
  print(f"{options['4']: ^35}")
  print(f"{options['5']: ^35}")
  print("")


while True:
  print_menu()
  option = input("Please chose an option... ").lower()
  if option == "1":
    os.system("clear")
    print_list()
  elif option == "2":
    os.system("clear")
    new_item = input("What would you like to add? ")
    todo_list.append(new_item)
    continue
  elif option == "3":
    os.system("clear")
    which = input("What would you like to edit? ")
    if which in todo_list:
      todo_list.remove(which)
      new_list_item = input("What do you want to change it to? ")
      todo_list.append(new_list_item)
  elif option == "4":
    os.system("clear")
    which = input("What would you like to delete? ")
    if which in todo_list:
      you_sure = input("Are you sure you want to delete this item? ")
      if you_sure == "yes":
        todo_list.remove(which)
      else:
        print("Okay, lets go back")
        continue
  elif option == "5":
    you_sure = input("Are you sure you want to delete the whole list? ")
    if you_sure == "yes":
      todo_list.clear()
    else:
      print("Okay, lets go back")
      continue
  else:
    os.system("clear")
    break
  continue
  # continue_loop = input("Want to continue? ")
  # if continue_loop != "yes":
  #   break
