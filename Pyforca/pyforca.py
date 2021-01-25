import artes
import palavras
from random import choice, randint

word_list = ["aardvark", "baboon", "camel"]
chosen_word = choice(word_list)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
lives = 6
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for char in range(len(chosen_word)):
  display.append('_')

while True:
  guess = str(input('Guess a letter: ').strip().lower())
  for index in range(len(chosen_word)):
    if guess == chosen_word[index]:
      display[index] = guess
    #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1.
  if guess not in chosen_word:
    lives -= 1 
  #If lives goes down to 0 then the game should stop and it should print "You lose."
  if lives == 0:
    print('You Lose.')
    break
  #Join all the elements in the list and turn it into a String.
  print(f"{' '.join(display)}")
  #Check if user has got all letters.
  if "_" not in display:
    print("You win.")
    break
  #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
  print(stages[lives])