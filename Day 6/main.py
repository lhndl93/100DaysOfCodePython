RED = "\033[31m"
END = "\033[0m"

print(f"{RED}LOGIN SYSTEM{END}")
print()

username = input("Username: ")
password = input("Password: ")

if username == "mark" and password == "password":
  print(f"{RED}Hello mark you beautiful man{END}")
elif username == "suzanne" and password == "password1":
  print(f"{RED}Hello suzanne you beautiful woman{END}")
elif username == "lee" and password == "password2":
  print(f"{RED}Hello lee you beautiful person{END}")
else:
  print(f"{RED}Go away!{END}")
  