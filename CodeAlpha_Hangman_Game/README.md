# Hangman Game 🎮

## Overview

Hangman Game is a simple command-line Python game where the player has to guess a hidden word one letter at a time. The game provides different difficulty levels, tracks wrong guesses, and gives the player a limited number of attempts.

## Features

* 🎯 Three Difficulty Levels (Easy, Medium, Hard)
* 🔤 Letter-by-letter word guessing
* ❌ Tracks incorrect guesses
* ⚠ Input validation for better user experience
* 🔄 Prevents duplicate guesses
* ❤️ 6 attempts to guess the word
* 🎉 Win and lose conditions
* 😊 Play Again option

## Technologies Used

* Python 3
* Random Module

## How to Run

1. Install Python 3.
2. Download or clone this repository.
3. Open the project folder in VS Code.
4. Open Terminal.
5. Run the following command:

```bash
python hangman.py
```

## How to Play

1. Select a difficulty level.
2. Guess one letter at a time.
3. If the letter is correct, it will be revealed in the word.
4. If the letter is wrong, one attempt will be deducted.
5. Guess the complete word before all attempts are used.

## Sample Output

```text
🎮 Welcome to Hangman Game!

Choose Difficulty:
1. Easy
2. Medium
3. Hard

Enter your choice (1/2/3): 2

Word: _ _ _ _ _ _
Wrong Letters:
Attempts Left: 6

Enter a letter: p
✅ Correct Guess!
```

## Learning Outcomes

* Python Basics
* Loops and Conditions
* Lists and Strings
* User Input Handling
* Random Module Usage
* Simple Game Development

## Future Improvements

* Add Hangman ASCII Art
* Add Score System
* Store Words in External File
* Add Timer Feature
* Automatic Play Again Functionality
