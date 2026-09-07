Stone Paper Scissors Game 🎮

A simple command-line Stone Paper Scissors game built using Python. The project allows the user to choose between stone, paper, or scissors while the computer randomly selects its choice. The program compares both choices and determines whether the user wins, the computer wins, or the game ends in a draw.

Features

Accepts the player's choice through user input.

Uses Python's random module to generate the computer's choice.

Uses dictionaries to map user inputs to game values and display names.

Compares the player's and computer's choices using conditional statements.

Displays the choices made by both the player and computer.

Determines and displays the final result: Win, Lose, or Draw.

Handles invalid choices with a wrong-choice message.

Concepts Used

Python variables

User input with input()

Conditional statements (if, elif, else)

Dictionaries

random.choice()

Comparison operators

f-strings

Basic game logic

How It Works

The program represents the three choices using numerical values:

Stone → 1

Paper → 0

Scissors → -1

The computer randomly selects one of these values, while the user enters s, p, or sc. The program then compares both choices and determines the winner according to the standard Stone-Paper-Scissors rules.

Example

enter your choice :s
computer choosed paper and you choosed stone
computer win

Technologies

Language: Python
Libraries: Random (built-in Python module)
Type: Command-Line Game
