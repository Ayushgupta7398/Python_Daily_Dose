# Python Program to illustrate Hangman Game

import random
from collections import Counter  # Used to count characters in a string

# Turn the long string of fruit names into a list
someWords = '''apple banana mango strawberry 
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''.split(' ')

def playagain():
    word = random.choice(someWords)
    letter_guessed = ''
    chances = len(word) + 2
    flag = 0

    print('\nWelcome to the Game!')
    print('Guess the word! HINT: The word is the name of a fruit.')

    # Display underscores for the word
    print(' '.join(['_' for _ in word]))

    try:
        while chances != 0 and flag == 0:
            print()
            guess = input('Enter a letter to guess: ').lower()

            if not guess.isalpha():
                print('⚠️ Please enter only a LETTER.')
                continue
            elif len(guess) > 1:
                print('⚠️ Please enter only ONE letter.')
                continue
            elif guess in letter_guessed:
                print("⚠️ You've already guessed that letter.")
                continue

            if guess not in word:
                print("❌ Think different!")
                chances -= 1
            else:
                print("✅ Good guess!")
                letter_guessed += guess * word.count(guess)

            # Print current word progress
            display_word = ''
            for char in word:
                if char in letter_guessed:
                    display_word += char + ' '
                else:
                    display_word += '_ '
            print('Word:', display_word.strip())
            print('Chances left:', chances)

            if Counter(letter_guessed) == Counter(word):
                print('\n🎉 Congratulations, You won!')
                print('The word was:', word)
                flag = 1
                break

        if chances <= 0 and Counter(letter_guessed) != Counter(word):
            print('\n💀 You lost! Try again.')
            print('The word was:', word)

    except KeyboardInterrupt:
        print('\n⛔ Game interrupted. Bye!')
        exit()

# ============ Game Loop =============

if __name__ == '__main__':
    while True:
        playagain()
        again = input('\nDo you want to play the game again? (y/n): ').lower()
        if again != 'y':
            print('Thanks for playing! 👋')
            break
