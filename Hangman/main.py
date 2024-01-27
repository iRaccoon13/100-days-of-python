import os, random


def cls():
  os.system('cls' if os.name == 'nt' else 'clear')


from hangman_words import word_list
from hangman_art import *

print(logo)
word = random.choice(word_list)
print("_" * len[word])
