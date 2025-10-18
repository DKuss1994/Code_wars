# Rock Paper Scissors! (8 kyu)

# https://www.codewars.com/kata/5672a98bdbdd995fad00000f/train/python
# Sprache: Python
# Datum: 2025-10-17

# Task: Rules of the "Rock, Paper, Scissors" game are:
#
# Rock beats Scissors
# Scissors beat Paper,
# Paper beats Rock.
# Let's play! You have to return which player won! In case of a draw return Draw!.

# example :
# "scissors", "paper" --> "Player 1 won!"
# "scissors", "rock" --> "Player 2 won!"
# "paper", "paper" --> "Draw!"

# Hier konnte ich meine Python Skills auffrischen.

def rps(p1:str, p2:str):
    p1 = p1.lower()
    p2 = p2.lower()

    if p1 ==p2:
        return "Draw!"
    elif p1 == "rock" and p2 == "scissors":
        return "Player 1 won!"
    elif p1 == "scissors" and p2 == "paper":
        return "Player 1 won!"
    elif p1 == "paper" and p2 == "rock":
        return "Player 1 won!"
    else:
        return "Player 2 won!"