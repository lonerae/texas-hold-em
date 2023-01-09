def reveal(deck, revealed, round):
    if (round == 1):
        deck.pop()
        for i in range(3):
            revealed.append(deck.pop())
    elif round == 2 or round == 3:
        deck.pop()
        revealed.append(deck.pop())
    return revealed

def fold(playerHands, playerBets, currentPlayer):
    playerHands[currentPlayer] = []
    playerBets[currentPlayer] = 0

def checkOrRaise(playerBets, playerCapitals, pot, playerBet, currentPlayer):
    playerBets[currentPlayer] += playerBet
    pot += playerBet
    playerCapitals[currentPlayer] -= playerBet

def endRound(numberOfPlayers, foldPlayersNumber, bet, playerBets, circle, lead, currentPlayer):
    return  (
                playerBets.count(bet) == numberOfPlayers - foldPlayersNumber and
                lead == (currentPlayer + 1) % numberOfPlayers and
                circle >= numberOfPlayers - foldPlayersNumber
            )

def giveValue(x):
    if x[0] == 'J':
        x[0] = 11
    elif x[0] == 'Q':
        x[0] = 12
    elif x[0] == 'K':
        x[0] = 13
    elif x[0] == 'A':
        x[0] = 14

def compare(x,y):
    return x[0]-y[0]

def calculatePower(allCards):
    for card in allCards:
        giveValue(card)

    allValues = []
    for i in range (len(allCards)):
        allValues.append([])
        allValues[i] = allCards[i][0]
    sorted(allValues)
    distinctValues = dict.fromkeys(set(allValues))
    
    for value in distinctValues.keys():
        distinctValues[value] = allValues.count(value)
    
    # DEBUG
    print(distinctValues)
    print("\n")

    power = 0
    for i in range(len(distinctValues)-1,-1,-1):
        if list(distinctValues.values())[i] == 4:
            comb = "4 * " + str(list(distinctValues.keys())[i])
            power = 4
        elif list(distinctValues.values())[i] == 3 and power < 3:
            comb = "3 * " + str(list(distinctValues.keys())[i])
            power = 3
        elif list(distinctValues.values())[i] == 2 and power < 2:
            comb = "2 * " + str(list(distinctValues.keys())[i])
            power = 2
        elif power < 1:
            comb = "1 * " + str(list(distinctValues.keys())[i])
            power = 1

    print(comb)
    print("\n")
