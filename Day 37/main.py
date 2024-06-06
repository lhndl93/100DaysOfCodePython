first_name = input("What is your first name? ").lower()
last_name = input("What is your last name? ").lower()
mothers_maiden_name = input("What is your mothers maiden name? ").lower()
birth_city = input("Where were you born? ").lower()

star_wars_first = first_name[0:3] + last_name[0:3]
star_wars_last = mothers_maiden_name[0:2] + birth_city[-3:]

print(f"{star_wars_first} {star_wars_last}".title())
