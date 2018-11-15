"""

Huddersfield Football Team

This program shows how many time the team has won, lost, drew and shows the total points from scoring.

The program that i have written accepts users integer inputs and using if statements adds them to their variables

"""

"""
__Author__ = Emaz Khan
__Email__ = U1859269@unimail.hud.ac.uk
__Date__ = Thursday 8th November 2018
"""

Count = 0
Wins = 0
Draws = 0
Losses = 0
Points = 0

for i in range(5):
    Count = Count + 1
    Match_Scored = int(input("Goals scored in match " + str(Count) + ": "))
    Match_Against = int(input("Opponent's goals in match " + str(Count) + ": "))
    Points = Points + Match_Scored
    if Match_Scored > Match_Against:
        Wins = Wins + 1
    elif Match_Scored == Match_Against:
        Draws = Draws + 1
    else:
        Losses = Losses + 1

print(" ")
print("Huddersfield Town")
print("Wins: " + str(Wins))
print("Losses: " + str(Losses))
print("Draws: " + str(Draws))
print("Points: " + str(Points))
