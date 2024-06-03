import os, time,random
listOfEmail = []

def send_email(max):
    for index in range(0,max): 
        time.sleep(1)
        os.system('clear')
        email_address = f"Hey {listOfEmail[index]},"
        message = "It has come to our attention that you're missing out on the amazing Replit 100 days of code. We insist you do it right away. If you don't we will pass on your email address to every spammer we've ever encountered and also sign you up to the My Little Pony newsletter, because that's neat. We might just do that anyway."
        sign_off_messages = ["Love and hugs", "Kisses and love", "Snuggles and buggles"]
        from_name = "Spamboy 2000"
        email_body = f"Email number {index + 1}\n{email_address}\n{message}\n{sign_off_messages[random.randint(0, len(sign_off_messages) - 1)]}\n{from_name}"
        print(email_body) 


def prettyPrint():
  os.system("clear") 
  print("listofEmail") 
  print()
  for index in range(len(listOfEmail)): 
    print(f"{index + 1}: {listOfEmail[index]}") 



while True:
  print("SPAMMER Inc.")
  menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
  if menu == "1":
    email = input("Email > ")
    listOfEmail.append(email)
  elif menu =="2":
    email = input ("Email > ")
    if email in listOfEmail:
      listOfEmail.remove(email)
  elif menu == "3":
    prettyPrint() 
  elif menu == "4":
    send_email(10)
  else:
    print("Wrong option, please chose again.")
  time.sleep(1)
  os.system("clear")
