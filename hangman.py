
import random

# Step 1: Predefined list of words
words = ["python", "hangman", "program", "developer", "keyboard"]

# Step 2: Randomly choose one word
word = random.choice(words)
word_letters = list(word)
guessed_letters = []
attempts = 6

print("🎯 Welcome to Hangman Game!")
print("Guess the word, one letter at a time!")
print("_ " * len(word))

# Step 3: Main game loop
while attempts > 0:
    guess = input("\nEnter a letter: ").lower()

    # Validate single alphabet input
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter only one alphabet letter.")
        continue

    # Avoid duplicate guesses
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    # Check guess correctness
    if guess in word_letters:
        print("✅ Good guess!")
    else:
        attempts -= 1
        print(f"❌ Wrong guess! Attempts left: {attempts}")

    # Display current word progress
    display = [letter if letter in guessed_letters else "_" for letter in word_letters]
    print(" ".join(display))

    # Check if the player has guessed all letters
    if "_" not in display:
        print("\n🎉 Congratulations! You guessed the word:", word)
        break

# Step 4: Game over condition
if attempts == 0:
    print("\n💀 Game Over! The correct word was:", word)
