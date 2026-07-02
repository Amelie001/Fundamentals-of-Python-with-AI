import random 
import string 

secret_set = set(random.sample(string.ascii_lowercase, 5))
guessed_letters = set()
attempts = 0 

print("Welcome to Guess the Secret Letters Game!")
print("I have selected 5 unique letters (a-z).")
print("Try to guess them!\n")

while guessed_letters != secret_set: 
    guess = input("Enter a letter: ").lower()
    attempts += 1 

    if len(guess) != 1 or guess not in string.ascii_lowercase: 
        print("Invalid input! Please enter one letter (a-z).")

    elif guess in guessed_letters: 
        print("You already guessed this letter!")

    elif guess in secret_set: 
        print("Correct guess!")
        guessed_letters.add(guess)

    else:
        print("Wrong guess, try again!")

    print("Your correct guesses so far:", guessed_letters)
    print()

print("Congratulations! You guessed all letters!")
print("Secret set was:", secret_set)
print("Total attempts:", attempts)