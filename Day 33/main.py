import os

list = []


def print_list():
  for item in list:
    print(item)


while True:
  option = input("Do you want to view, add or edit your todo list? ").lower()
  if option == "view":
    print_list()
  elif option == "edit":
    which = input("What would you like to edit? ")
    if which in list:
      list.remove(which)
      new_list_item = input("What do you want to change it to? ")
      list.append(new_list_item)
  elif option == "add":
    new_item = input("What would you like to add? ")
    list.append(new_item)
    continue 
  else:
    os.system("clear")
    break