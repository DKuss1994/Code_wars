# Street Fighter 2 - Character Selection (6 kyu)

# https://www.codewars.com/kata/5853213063adbd1b9b0000be/train/python
# Sprache: Python
# Datum: 2025-10-18

# Task: n this kata, you simulate the character selection screen from Street Fighter 2.
#
# You’re given:
#
# A 2x6 grid of fighter names.
#
# An initial cursor position (top-left is (0, 0)).
#
# A list of moves (up, down, left, right).
#
# Your task is to return the list of fighters hovered over after each move.
#
# Rules:
#
# The cursor wraps horizontally (moving left from the first column jumps to the last, and vice versa).
#
# The cursor does not wrap vertically (you can’t move above the top row or below the bottom row).
#
# Example:
# If the cursor starts at Ryu and the moves are ['up', 'left', 'right', 'left', 'left'],
# the result should be ['Ryu', 'Vega', 'Ryu', 'Vega', 'Balrog'].

# In this kata, I improved my understanding of list comprehensions
# by using them to track the fighters’ positions after each move.

def street_fighter_selection(fighters, initial_position, moves):
    # Hier kommen die Fighter rein wo wir darauf gemovet haben
    fighters_move = []
    # Hier nehmen die Postion aus dem Tupel und geben jeweil die erste für hoch und runter
    # und die zweite Zahl für links und rechts
    up_down, left_right = initial_position
    #Hier gehen wir mit der for Schleife durch die liste der moves.
    for bewegung in moves:
        # Prüfung, ob wir up hier haben und die Sonderbedienung eintritt, dass wir uns nicht bewegen, wenn wir oben sind.
        if bewegung == "up" and up_down == 0:
            fighters_move.append(fighters[up_down][left_right])
        # Prüfen ob wir up haben und nach oben moven in dem wir von 1 auf 0 gehen
        elif bewegung == "up" and up_down == 1:
            up_down = 0
            fighters_move.append(fighters[up_down][left_right])
        elif bewegung == "down" and up_down == 0:
            up_down = 1
            fighters_move.append(fighters[up_down][left_right])
        elif bewegung == "down" and up_down == 1:
            fighters_move.append(fighters[up_down][left_right])
        elif bewegung == "left" and left_right == 0:
            left_right = len(fighters[up_down]) - 1
            fighters_move.append(fighters[up_down][left_right])
        elif bewegung == "left" and left_right == 0:
            left_right = len(fighters[up_down]) - 1
            fighters_move.append(fighters[up_down][left_right])
        elif bewegung == "left":
            left_right -= 1
            fighters_move.append(fighters[up_down][left_right])
        elif bewegung == "right" and len(fighters[up_down]) - 1 == left_right:
            left_right = 0
            fighters_move.append(fighters[up_down][left_right])
        elif bewegung == "right":
            left_right += 1
            fighters_move.append(fighters[up_down][left_right])
    return fighters_move
