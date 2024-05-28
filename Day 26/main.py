import os
import time
import pygame

pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound('audio.wav')
sound.play()
sound.stop()

def pause():
  pygame.mixer.pause()
  

def play():
  # Play the sound
  pygame.mixer.unpause()
  while True:
    option_playing = int(input("Press 2 to pause at any time.. "))
    if option_playing == 2:
      pause()
      break
    
while True:
  # Show the menu
  print("MUSIC PLAYER!!")
  os.system("clear")
  time.sleep(2)
  print("""
  Please select from the below -
  1. Play
  2. Exit
  """)
  option = int(input("What option are you choosing? "))
  if option == 1:
    play()
  else:
    exit()

