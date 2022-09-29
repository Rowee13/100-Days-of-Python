# HANGMAN GAME

import random
from hangman_word import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

from hangman_art import logo, stages

print(logo)

# for testing
print(f"The chosen word is: {chosen_word}")

# blank letters
display = []
for _ in range(word_length):
    display += "_"

# Guessing Loop
end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already  guessed {guess}")

    # checking of guessed letters
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\nCurrent letter: {letter}\nGuessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose!")

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win!")

    print(stages[lives])
