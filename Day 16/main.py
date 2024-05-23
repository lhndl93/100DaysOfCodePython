print("GUESS THE LYRICS")

counter = 1
song = "Never going to ..... you up"
print(song)
print()

while True:
  guess_song = input("What lyric is missing? ").lower()
  if guess_song == "give":
    print("Congrats!!! Never going to give you uppppp")
    print(f"This took you {counter} attempts..")
    break
  else:
    print("Wrong, try again..")
    counter += 1
    
  