from time import time
import random, os, sys
from GuessTheNumberArt import logo
import GuessTheNumberModeSpecific as modeSpecific
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from loading import loading_screen
loading_screen(logo, 500)
while True:
  print("""
______________________
| 1. | Free Play     |
| 2. | Timed         |
| 3. | Limited Tries |
^^^^^^^^^^^^^^^^^^^^^^""")
  mode = input("What mode would would you like to play? Input the number from the table. \n\n: ")
  try:
    int(mode)
  except: 
    print("Invalid input. ")
  else: 
    mode = int(mode)
    break
lives = 999999 if mode == 1 else lives = 10
