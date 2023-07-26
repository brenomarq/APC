# Guess the secret word
import os

secret_word = "mischievous"
trials = 3
typed_letters = []

print("GUESS THE SECRET WORD!")
print("Enjoy this simple little game in Python.")
while True:
    letter = input("Guess a letter: ")

    if trials == 0:
        print("You lose! You wasted all of your chances! :(")
        break

    if len(letter) != 1:
        print("You must type only one letter!")
        continue

    if not letter.isalpha():
        print("You must type a valid character!")
        continue

    typed_letters.append(letter)
    temporary_word = ""
    for l in secret_word:
        if l in typed_letters:
            temporary_word += l
        else:
            temporary_word += "*"

    if letter not in secret_word:
        print(f"Your progress: {temporary_word}")
        trials -= 1
        continue

    if temporary_word == secret_word:
        os.system("cls")
        print("Congratulations! You guessed the secret word!")
        print(f"The secret word was {secret_word}")
        break

    print(f"Your progress: {temporary_word}")
