import os
import random
import time

def random_number():
  return random.randint(0, len(greetings) - 1)

greetings = ["Bonjour", "Hola", "Zdravstvuyte", "Nǐn hǎo	", "Salve", "Konnichiwa", "Guten Tag", "Olá", "Anyoung haseyo", "Asalaam alaikum", "Goddag", "Shikamoo", "Goedendag", "Yassas", "Dzień dobry", "Selamat siang", "Namaste, Namaskar", "God dag", "Merhaba", "Shalom", "God dag"]

print(greetings[random_number()])

# how_many = int(input("How many random greetings would you like? "))
# for _ in range(how_many):
#   print(greetings[random_number()])

