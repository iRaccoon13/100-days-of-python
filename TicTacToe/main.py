from hangman_artTicTacToeArt import logo, board
import os,random,sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from loading import loading_screen
loading_screen(logo,500)
# Clear console
def cls():
  os.system('cls' if os.name == 'nt' else 'clear')
print(board)