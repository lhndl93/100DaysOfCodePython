# Correctly ready instructions
usernameList = ["david", "luke", "lee"]
password = "Password123"

def login():
    while True:
        usernameInput = input("What is your Username? ")
        if usernameInput in usernameList:
            while True:
                passwordInput = input("What is your Password? ")
                if passwordInput == password:
                    print("Hello!", usernameInput)
                    return
                else:
                    print("Incorrect Password, please try again.")
        else:
            print("Incorrect Username :(")
        
login()
        
            
    