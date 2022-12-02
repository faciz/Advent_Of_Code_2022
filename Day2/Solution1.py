# A X Rock
# B Y Paper
# C Z Scissors

def getWinner(player1, player2):
    #Draw
    if ord(player2) - ord(player1) == 23:
        return "Draw"
    #Player 1 plays rock
    if player1 == "A":
        if player2 == "Y":
            return "Player2"
        if player2 == "Z":
            return "Player1"
    #Player 1 plays paper
    if player1 == "B":
        if player2 == "X":
            return "Player1"
        if player2 == "Z":
            return "Player2"
    #Player 1 plays scissors
    if player1 == "C":
        if player2 == "X":
            return "Player2"
        if player2 == "Y":
            return "Player1"

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
    moves = line.split()
    if getWinner(moves[0], moves[1]) == "Player1":
        totalScore += moveScore(moves[1])
    elif getWinner(moves[0], moves[1]) == "Player2":
        totalScore += moveScore(moves[1]) + 6
    else:
        totalScore += moveScore(moves[1]) + 3

print(totalScore)
