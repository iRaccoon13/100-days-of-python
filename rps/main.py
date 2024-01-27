rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

from random import randint as r

asciilist = [rock, paper, scissors]
rps = ["rock", "paper", "scissors"]

choice = int(input("Rock, Paper, or Scissors? \n 1: Rock \n 2: Paper \n 3: Scissors \n"))
if choice not in range(1, 4):  # Use range() to check for valid input
    print("Oops! Please enter a valid number (1, 2, or 3).")
    exit(1)

ascii = asciilist[choice - 1]  # Adjust index for list starting at 0
print(f"You chose: \n{ascii}")
cpuchoice = r(1, 3)
ascii = asciilist[cpuchoice - 1]  # Adjust index for list starting at 0
print(f"CPU chose \n{ascii}")

# Determine winner based on choices
if choice == 1 and cpuchoice == 3:  # You: Rock, CPU: Scissors
    print("You win! ✊✂️")
elif choice == 2 and cpuchoice == 1:  # You: Paper, CPU: Rock
    print("You win! 🪨")
elif choice == 3 and cpuchoice == 2:  # You: Scissors, CPU: Paper
    print("You win! ✌️")
elif choice == cpuchoice:  # Tie
    print("It's a tie! ")
else:  # You lose
    print("You lose! ")

