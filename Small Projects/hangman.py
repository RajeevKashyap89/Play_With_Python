import random
from hangman_words import word_list
from hangman_art import *

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo3)
print('\n To win, guess the word before the person is hung.\n')

display = []
wrong_guesses = []

for i in range(word_length):
    display.append('_')

while not end_of_game:
    guess = input('Guess Letter: ').lower()

    if guess in wrong_guesses:
        print(f"{' '.join(display)}")
        print(stages[lives])
        print(f"you've already guessed with the letter '{guess}', pick another letter.")
    else:
        wrong_guesses.append(guess)

        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        print(f"{' '.join(display)}")

        if '_' not in display:
            end_of_game = True
            print('\n Genius, genius, genius! you won!') 
            print(logo2) 

        if guess not in chosen_word:
            lives -= 1

        if not end_of_game:
            print(stages[lives])
            if guess not in chosen_word:
                print(f"'{guess}' is not in the word, you lost 1 life.")

        if lives == 0:
            end_of_game = True
            print('You lose.')
            print(f"\n The word was'{chosen_word}'")                              