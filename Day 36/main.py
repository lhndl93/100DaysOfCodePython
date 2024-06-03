import os
name_list = []

def print_list():
  for i in name_list:
    print(f"{name_list.index(i) + 1} {i}")

while True:
  first_name = input("What is your first name > ").strip().capitalize()
  last_name = input("What is your last name > ").strip().capitalize()
  full_name = (f"{first_name} {last_name}")
  
  if full_name not in name_list:
    os.system('clear')
    name_list.append(full_name)
    print_list()
    
  else:
    os.system('clear')
    print_list()
    print("ERROR: duplicate")
    
  create_more = input("Do you want to create another? ").strip().lower()
  if create_more == "yes":
    os.system('clear')
    continue
  else:
    break
    
  