import subprocess
games = ["Hangman","Tic Tac Toe","Rock Paper Scissors","Guess The Number"]
gamemenu = """"""
gamemenu += "_"*len(max(games, key=len))
gamemenu += "_"*10+"\n"
for i in games:
  gamemenu += f"| {games.index(i)}. |{i}"
  gamemenu += " "*(len(max(games, key=len))-len(i)) + "  |\n"
gamemenu += ("^"*len(max(games, key=len)+"  |"+ "_"*10))+ "\n"
print(gamemenu)
choice = input("What would you like to play? \nEnter the number. \n\n: ")
None if choice.isdigit() else print("Invalid input")
files = {
  "Hangman": "Hangman/main.py",
  "Tic Tac Toe": "TicTacToe/main.py",
  "Rock Paper Scissors": "rps/main.py",
  "Guess The Number": "GuessTheNumber/main.py"
}
subprocess.run(["python", files[games[int(choice)]]])