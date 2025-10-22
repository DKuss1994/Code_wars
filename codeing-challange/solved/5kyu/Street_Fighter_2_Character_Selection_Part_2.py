# Street Fighter 2 (5 kyu)

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
    # Hier erstellen wir die Liste wo der Move die Person hinbewegt
    list_fighters = []
    # Ist ein Dictonary wo wir den Schlüssel aus move bekommen und den zu Ordnen können. Da man in Listen um nach rechts zu
    # kommen den Index hochsetzten muss und nach links Index nach unten setzt muss hat left und right -1 und 1
    # Wir Verwenden hier auch ein X Y Kordinatensystem die erste Zahl steht für die Y -Achse und die Zweite für X -Achse
    Moves = {
        "up": [-1, 0],
        "down": [1, 0],
        "left": [0, -1],
        "right": [0, 1],
        "": [0, 0]
    }
    #Hier nehmen wir auch den Parameter positions und spilten den in 2 Variabeln unseren y-Asche und x-Asche diese sind unsere
    #Hauptwerte mit der wir im index arbeiten werden
    y, x = positions
    # Wir edetieren in den Parameter moves da diese uns zeigt wo der Usere sein Maus oder ähnliches Bewegt.
    for bewegung in moves:
        # Durch unsere Dictonary können wir die moves als Schlüssel benutzen und dy Y+ Asche und dx unsere X+ Achse erstellen
        #Wir gereifen darauf zu beispiel bewegung geht durch die Liste durch bewegung = "right" dann schauen wir in unsere
        # Dictonary und bekommen den wert 0,1 den wir in dy = 0 und dx = 1 speichern

        dy, dx = Moves[bewegung]
        # Wir adieren jetzt die move bewegung zu den index Achsen dazu
        y += dy
        x += dx
        # Hier wird geprüft ob oben oder unten außerhalb des Index ist. Da wir ja eine Sonderbediengung haben
        x, y = out_off_index(bewegung, dx, dy, fighters, x, y)
        x, y = hit_space(bewegung, dx, dy, fighters, x, y)
        x, y = out_off_index(bewegung, dx, dy, fighters, x, y)

        list_fighters.append(fighters[y][x])

    return list_fighters


def hit_space(bewegung, dx, dy, fighters, x, y) -> Any:
    if fighters[y][x] == "":
        if bewegung == "left" or bewegung == "right":
            # Bei rechts oder links leerzeichen machen wir einfach das gleiche noch mal und soweit gehen, bis wir kein
            # kein leerzeichen haben.
            x += dx

        elif bewegung == "up" or bewegung == "down":
            # Und bei oben oder unten sollen wir ja stehen bleiben
            y -= dy
    return x, y


def out_off_index(bewegung, dx, dy, fighters, x, y):
    if y < 0 or y > len(fighters) - 1:
        if bewegung == "up" or bewegung == "down":
            # Damit wir die Sonderbediengung erfüllen ziehen wir das gleiche nochmal ab und sind bei der Ausgangspositon
            y -= dy
    # Hier wird geprüft ob rechts oder links außerhalb des Index ist. Da wir ja hier eine Sonderbediengung haben.
    if x < 0 or x > len(fighters[y]) - 1:
        if bewegung == "right":
            # Ist move rechts und wir sind außerhalb des Index wird der index auf null gesetzt also alle auf Anfang.
            x = 0
            # Hier wird noch einmal geprüft ob es ein leerzeichen gibt damit wir das überspringen.

            if fighters[y][x] == "":
                x += dx
        elif bewegung == "left":
            # Ist move links und wir sind außerhalb des Index wird der index auf die letzte Stelle gesetzt von der Liste.
            # Wenn wir -1 nehmen würden würde unsere Dictonary nicht mehr funktionieren deswegen len
            x = len(fighters[y]) - 1
            # Hier wird noch einmal geprüft ob es ein leerzeichen gibt damit wir das überspringen.
            if fighters[y][x] == "":
                x += dx
                # Hier wird geprüft was passiert, wenn man auf ein Leerzeichen trifft.
    return x, y

