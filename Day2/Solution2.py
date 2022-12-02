# A Rock
# B Paper
# C Scissors

# X Lose
# Y Draw
# Z Win

def getScore(player1, outcome):
    #Player 1 plays rock
    score = 0
    if outcome == "X":
        if player1 == "A":
            score = 3
        if player1 == "B":
            score = 1
        if player1 == "C":
            score = 2
        return score
    if outcome == "Y":
        if player1 == "A":
            score = 1
        if player1 == "B":
            score = 2
        if player1 == "C":
            score = 3
        return score + 3
    if outcome == "Z":
        if player1 == "A":
            score = 2
        if player1 == "B":
            score = 3
        if player1 == "C":
            score = 1
        return score + 6


def moveScore(move):
    if move == "X":
        return 1
    elif move == "Y":
        return 2
    else: 
        return 3

f = open("input.txt","r")
lines = f.readlines()
totalScore = 0

for line in lines:
    line = line.replace("\n","")
    line = line.split()
    totalScore += getScore(line[0], line[1])

print(totalScore)
