import random

words = {
    "Easy": ["apple", "book", "tree", "fish"],
    "Medium": ["python", "school", "mobile", "garden"],
    "Hard": ["computer", "elephant", "developer", "keyboard"]
}

print("🎮 Welcome to Hangman Game!")

# Difficulty Selection
print("\nChoose Difficulty:")
print("1. Easy")
print("2. Medium")
print("3. Hard")

choice = input("Enter your choice (1/2/3): ")

if choice == "1":
    word = random.choice(words["Easy"])
elif choice == "2":
    word = random.choice(words["Medium"])
else:
    word = random.choice(words["Hard"])

guessed_letters = []
wrong_letters = []
attempts = 6

while attempts > 0:
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Wrong Letters:", " ".join(wrong_letters))
    print("Attempts Left:", attempts)

    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    # Input Validation
    if len(guess) != 1 or not guess.isalpha():
        print("⚠ Please enter only one alphabet letter!")
        continue

    if guess in guessed_letters or guess in wrong_letters:
        print("⚠ You already guessed that letter!")
        continue

    if guess in word:
        guessed_letters.append(guess)
        print("✅ Correct Guess!")
    else:
        wrong_letters.append(guess)
        attempts -= 1
        print("❌ Wrong Guess!")

if attempts == 0:
    print("\n💀 Game Over!")
    print("The word was:", word)

# Play Again Option
play_again = input("\nDo you want to play again? (yes/no): ").lower()

if play_again == "yes":
    print("Restart the program to play again!")
else:
    print("Thanks for playing! 😊")