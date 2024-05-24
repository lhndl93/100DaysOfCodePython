print("Math Game!!")
print()

# Ask the user for the multiples they want to practice
multiples = int(input("What multiples do you want to do? "))

counter = 0

# Loop through numbers 1 to 10
for i in range(1, 11):
    question = int(input(f"{i} X {multiples} = "))
    
    # Check if the answer is correct
    if question == i * multiples:
        print("That is correct! Next question..")
        counter += 1
    else:
        print("That wasn't right :(")
        break

# Check if the user got all questions correct
if counter == 10:
    print(f"Perfect score!! You got {counter} out of 10!!")
else:
    print(f"Not so perfect, but close! You got {counter} out of 10!!")
