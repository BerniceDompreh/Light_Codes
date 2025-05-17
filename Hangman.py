# Creating a hangman quiz

import random

# The List of words to be quizzed on
fruits = ["pineapple", "banana", "orange", "guava", "pear"]

# Choosing a random word from the list of fruits.
quiz_word = random.choice(fruits)

# This is to display the spaces in the word to be filled.
display = ['_' for _ in quiz_word]
attempts = 3

print("Welcome to Hangman")

while attempts > 0 and '_' in display:
    print('_'.join(display))  # this is to display the current word.
    guess = input("\nGuess a letter: ")
    # This takes the input of the words in lower case letters.
    print(guess.lower())

# This part of the code displays the word with is inputs in the spaces.

    if guess in quiz_word:
        for process, word in enumerate(quiz_word):
            if word == guess:
                display[process] = guess

    else:
        print("Error")
        attempts -= 1

if '_' not in display:
    print('_'.join(display))
    print("Hurrayyy!!!")
    print()
    print("You had it right")

else:
    print("You lost. The word is:", quiz_word)

print("Re-run the code to move to the next word.")
