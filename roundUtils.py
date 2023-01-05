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

def calculatePower(allCards):
    print(allCards)