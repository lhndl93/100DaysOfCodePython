print("LIST GENERATOR")
print()

start_at = int(input("What number should we start at? "))
stop_at = int(input("What number should we stop at? "))
increments = int(input("What increments should we use? "))

for i in range(start_at, stop_at + 1, increments):
   print(i)
  