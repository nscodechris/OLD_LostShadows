

import random
import time

words = ['kindly', 'recite', 'repeat', 'tree', 'display', 'geeks', 'coader', 'programmer', 'python', 'premium', 'watch']
word = random.choice(words)
correct_word = word
spaces = ['_'] * len(word)
num_turns = 10
count = 0

def get_letter_position(guess, word, spaces):
    index = -2
    while index != -1:
        if guess in word:
            index = word.find(guess)
            # print(index)
            removed_character = '*'
            word = word[:index] + removed_character + word[index + 1:]
            # print(word)
            spaces[index] = guess
        else:
            index = -1

    return (word, spaces)


def win_check():
    for i in range(0, len(spaces)):
        if spaces[i] == '_':
            return -1

    return 1

def hang_man_print(count):
    if count == 1:
        time.sleep(1)
        print("   _____ \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "__|__\n")
    elif count == 2:
        time.sleep(1)
        print("   _____ \n"
              "  |     | \n"
              "  |     |\n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "__|__\n")
    elif count == 3:
        time.sleep(1)
        print("   _____ \n"
              "  |     | \n"
              "  |     |\n"
              "  |     | \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "__|__\n")
    elif count == 4:
        time.sleep(1)
        print("   _____ \n"
              "  |     | \n"
              "  |     |\n"
              "  |     | \n"
              "  |     O \n"
              "  |      \n"
              "  |      \n"
              "__|__\n")
    elif count == 5:
        time.sleep(1)
        print("   _____ \n"
              "  |     | \n"
              "  |     |\n"
              "  |     | \n"
              "  |     O \n"
              "  |    /|\ \n"
              "  |    / \ \n"
              "__|__\n")


def main_game(num_turns, word, spaces, count):
    while num_turns > 0:
        guess = input('Guess a character:')

        if guess in word:
            word, spaces = get_letter_position(guess, word, spaces)
            # print(spaces)
            num_turns -= 1
        else:
            print('Sorry that letter is not in the word.')
            num_turns -= 1
            if num_turns % 2 == 0:
                count += 1
                hang_man_print(count)

        if win_check() == 1:
            print('Congratulations you won')
            break
        if num_turns == 0:
            count = 5
            hang_man_print(count)
            print(f"You loose, correct word is: {correct_word}")
            break
        print(f'you have {num_turns} turns left.')
        print()

