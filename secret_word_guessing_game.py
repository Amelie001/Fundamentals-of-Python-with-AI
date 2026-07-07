secret_words = {"apple", "tiger", "red", "beach", "music"}
guessed_words = set()
attempts = 10

print("Welcome to the Unique Secret Word Guessing Game!")
print("Guess the 5 secret words. You have 10 attempts.")

while attempts > 0 and len(guessed_words) < 5:
    guess = input("Guess a word: ").lower()

    if guess in guessed_words:
        print("You already guessed this word.")
    elif guess in secret_words:
        guessed_words.add(guess)
        print("Correct!")
    else:
        attempts -= 1
        print("Wrong! Attempts left:", attempts)

    print("Words found:", len(guessed_words), "/ 5")

if len(guessed_words) == 5:
    print("You won! You guessed all the words!")
else:
    print("Game over!")
    print("The secret words were:", secret_words)