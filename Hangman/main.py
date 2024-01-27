from hangman_art import logo, stages
from hangman_words import word_list
import os,random,sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from loading import loading_screen
#from time import time
loading_screen(logo,500)
# Clear console
def cls():
  os.system('cls' if os.name == 'nt' else 'clear')
def nothing():
  pass
word = random.choice(word_list)
lives = 6
display = []
lettersguessed = []
wordguessed = False
firstguess = True
formatted_display = ""
while lives > 0 and not wordguessed:
  cls()
  print(logo)
  livespunc = "!" if lives < 3 else "."
  print("_ " * len(word)) if firstguess else print(formatted_display)
  guess_allowed = False
  while not guess_allowed:
    guess = input(f"\nGuess?- {lives} lives left{livespunc} \n\n:").lower()
    if len(guess) == 1:
      guess_allowed = True
    else:
      cls()
      print(logo)
      print("Please enter a single letter.")
      input("Press enter to continue. ")
      cls()
  if guess in lettersguessed:
    cls()
    print(logo)
    print(f"You already guessed {guess}!")
    input("Press enter to continue. ")
  else:
    firstguess = False
    #check guess
    try: 
      word.index(guess)
    except ValueError:
      lives -= 1
      if lives == 0:
        break
      cls()
      print(logo)
      print(f"Wrong! {lives} lives left{livespunc}\nPress enter to try again!\n")
      input(stages[lives])
      lettersguessed.append(guess)
    else:
      cls()
      print(logo)
      print(f"Correct! {lives} lives left{livespunc}\nPress enter to continue!")
      lettersguessed.append(guess)
      input()
    #check if word is guessed and setup display
    display = []
    for i in word:
      display.append("_ ") if i not in lettersguessed else display.append(i)
    formatted_display = ""
    for i in display:
      formatted_display += i
    wordguessed = bool("_" not in display)
if wordguessed:
  print(f"You won! The word was {word}!")
else:
  print(f"You lost! The word was {word}!")
input("Press enter to go home. ")