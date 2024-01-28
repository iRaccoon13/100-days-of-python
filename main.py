import subprocess
games = ["Exit", "Hangman","Tic Tac Toe","Rock Paper Scissors","Guess The Number"]
gamemenu = """"""
gamemenu += "_"*len(max(games, key=len))
gamemenu += "_"*10+"\n"
for i in games:
  gamemenu += f"| {games.index(i)}. |{i}"
  gamemenu += " "*(len(max(games, key=len))-len(i)) + "   |\n"
gamemenu += ("^"*(len(max(games, key=len))+10)) + "\n"
while True:
  print(gamemenu)
  choice = input("What would you like to play? \nEnter the number. \n\n: ")
  None if choice == "" else print("Invalid input")
  try: 
    choice = int(choice)
  except:
    print("Invalid input")
    continue
  files = {
    "Hangman": "Hangman/main.py",
    "Tic Tac Toe": "TicTacToe/main.py",
    "Rock Paper Scissors": "rps/main.py",
    "Guess The Number": "GuessTheNumber/main.py"
}
  exit(0) if int(choice) == 0 else False
  subprocess.run(["python", files[games[int(choice)]]])
