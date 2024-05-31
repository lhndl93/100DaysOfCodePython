import time

def text_color(color):
  if color == "red":
    return ("\033[31m")
  elif color == "blue":
    return ("\033[34m")
  elif color == "green":
    return ("\033[32m")
  elif color=="white":
    return ("\033[0m")
  elif color == "purple":
    return ("\033[35m")
  elif color=="yellow":
    return ("\033[33m")
  else:
    return ("\033[00m")
    

prev = "PREV"
next = "NEXT"
pause = "PAUSE"

title = f"{text_color('red')} =\
{text_color('reset')}=\
{text_color('blue')}=\
{text_color('green')} Music App\
{text_color('blue')} =\
{text_color('reset')}=\
{text_color('red')}="

print(f"        {title:^35}")
print(f"🔥▶️\t{text_color('white')}Radio Gaga")
print(f"\t{text_color('yellow')}Queen" )
print("")
print(f"{text_color("white")} \t {prev: <35}")
print(f"{text_color("green")} \t {pause: ^35}")
print(f"{text_color("purple")} \t {next: >35}")

text = f"{text_color('white')}WELCOME TO"
print(f"{text: ^35}")
time.sleep(0.5)
text = f"{text_color('blue')}==  ARMBOOK  =="
print(f"{text: ^35}")
time.sleep(0.5)
text = f"{text_color('yellow')}Definitely not a rip off"
print(f"{text: >35}")
time.sleep(0.5)
text = f"{text_color('yellow')}of a different soial network"
print(f"{text: >35}")
time.sleep(0.5)
text = f"{text_color('red')}Honest."
print(f"{text: ^35}")
time.sleep(0.5)
print("")
text = f"{text_color('white')}Username: "
print(f"{text: ^35}")
time.sleep(0.5)
text = f"{text_color('white')}Password: "
print(f"{text: ^35}")

