#1. Pick a word
#2. How to check user's answers
#3. Replace blanks with guesses
#4. Check if user has won
#5. Keep track of user's life
import random

from hangman_art import *
from hangman_words import *
print(logo)
end_of_game = False
lives = 6
word = random.choice(word_samples)
word_len = len(word)

#generate blanks
blanks = []
for _ in range(word_len):
  blanks.append("_")
print(blanks)

#check user's guess

while not end_of_game:
  user_input = input("Guess a letter: ").lower()
  for position in range(word_len):
  #get user's guess
    letter = word[position]
    if letter == user_input:
      blanks[position] = letter
  if user_input not in word:
    lives -= 1
    if lives == 0:
      end_of_game = True
      print("You lose!")
      
  print(blanks)

    #check if no more "_" are left in 'blanks'. Then all letters have been guessed
  if "_" not in blanks:
    end_of_game = True
    print("You win!")
    print(f"The word is {word}")
  print(stages[lives])
  
    
    
    