# Counting Duplicates (6 kyu)

# https://www.codewars.com/kata/58583922c1d5b415b00000ff
# Sprache: Python
# Datum: 2025-10-20

# Task: You need to simulate a character selection cursor on a 2D grid (like in a fighting game).
#
# The grid can be any rectangular size and may contain empty spaces ("") that are not selectable.
#
# The cursor starts at a given initial position (a non-empty slot).
#
# You get a list of moves (up, down, left, right).
#
# When moving:
#
# Left/right: wrap around horizontally but skip empty spaces.
#
# Up/down: move vertically only if the target cell isn’t empty — otherwise, stay where you are.
#
# The result should be a list of the fighters’ names the cursor lands on after each move.

# Ich hab gelernt, wie man Zeichen in einem String einmal zählt, wenn sie mehr als einmal drin vorkommen.
def super_street_fighter_selection(fighters: list[str], positions: tuple[int, int], moves: list[str]):
    list_fighters = []
    Moves = {
        "up": [-1, 0],
        "down": [1, 0],
        "left": [0, -1],
        "right": [0, 1],
        "": [0, 0]
    }
    y, x = positions
    for bewegung in moves:
        dy, dx = Moves[bewegung]
        y += dy
        x += dx
        # Hier wird geprüft ob oben oder unten außerhalb des Index ist
        if y < 0 or y > len(fighters) - 1:
            if bewegung == "up" or bewegung == "down":
                y -= dy
        # Hier wird geprüft ob rechts oder links außerhalb des Index ist.
        if x < 0 or x > len(fighters[y]) - 1:
            if bewegung == "right":
                x = 0

                if fighters[y][x] == "":
                    x += dx
            elif bewegung == "left":
                x = len(fighters[y]) - 1
                if fighters[y][x] == "":
                    x += dx
                    # Hier wird geprüft was passiert, wenn man auf ein Leerzeichen trifft.
        if fighters[y][x] == "":
            if bewegung == "left" or bewegung == "right":
                x += dx

            elif bewegung == "up" or bewegung == "down":
                y -= dy
        if y < 0 or y > len(fighters) - 1:
            if bewegung == "up" or bewegung == "down":
                y -= dy
        # Hier wird geprüft ob rechts oder links außerhalb des Index ist.
        if x < 0 or x > len(fighters[y]) - 1:
            if bewegung == "right":
                x = 0

                if fighters[y][x] == "":
                    x += dx
            elif bewegung == "left":
                x = len(fighters[y]) - 1
                if fighters[y][x] == "":
                    x += dx

        list_fighters.append(fighters[y][x])

    return list_fighters

