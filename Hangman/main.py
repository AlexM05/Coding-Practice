from os import system, name
from random import randint

hangman_pics = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''']


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def random_word():
    with open("words.txt", "r") as word_list:
        lines = word_list.readlines()
        word = lines[randint(0, len(lines) - 1)].strip()
    return word


def main():
    word = random_word()
    attempts = 6
    used_words = []
    current_state = ["_" for _ in word]
    print(word)
    while "_" in current_state and attempts > 0:
        clear()
        print(hangman_pics[attempts])
        print(used_words)
        print("\n")
        print(' '.join(current_state))
        current_letter = input("Please enter a letter: ").lower()
        if current_letter in used_words:
            print("You have already used this letter.")
            continue

        used_words.append(current_letter)
        if current_letter in word:
            for index, letter in enumerate(word):
                if letter == current_letter:
                    current_state[index] = current_letter
        else:
            attempts -= 1

    clear()
    if attempts != 0:
        print(f"You win! The word was {word}")
    else:
        print(hangman_pics[0])
        print(f"You lose! The word was {word}")

    input("Press enter to exit: ")


if __name__ == "__main__":
    main()
