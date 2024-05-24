# Misread the instructions and instead of doing one fuction, I created functions for the Username and Password input

usernameList = ["david", "luke", "lee"]
password = "Password123"

def yourUsername():
  return input("What is your username? ")

def yourPassword():
  return input("What is your password? ")

while True:
  if yourUsername() in usernameList:
    if yourPassword() == password:
      print("Hello!! welcome")
    else:
      print("Wrong Password. Please try again.")
  else:
    print("Wrong username, try again.")
    