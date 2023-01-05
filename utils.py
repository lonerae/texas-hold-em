import random

FIGURES = ['J','Q','K']
VALUES = list(range(1,11)) + FIGURES
SIGNS = ['♡','♤','♧','♢']

CAPITAL = 1000

def instantiateCapitals(numberOfPlayers):
    playerCapitals = []
    for i in range(0,numberOfPlayers):
            playerCapitals.append(CAPITAL)
    return playerCapitals

def capitalRemains(playerCapitals, numberOfPlayers):
    return playerCapitals.count(0) < numberOfPlayers - 1

def shuffleDeck():
    deck = []
    for s in SIGNS:
        for v in VALUES:
            deck.append([v,s])
    random.shuffle(deck)
    return deck

def serveCards(numberOfPlayers, deck):
    hand = []
    for p in range(0,numberOfPlayers):
        hand.append([])
    for i in range(0,2):
        for p in range(0,numberOfPlayers):
            hand[p].append(deck.pop())
    return hand

def instantiateBets(numberOfPlayers):
    playerBets = []
    for p in range(0,numberOfPlayers):
        playerBets.append(0)
    return playerBets

def resetGame(bigBlindPlayer):
    currentPlayer = bigBlindPlayer
    bet = 0
    pot = 0
    round = 0
    firstBet = True
    foldPlayersNumber = 0
    roundStart = True
    revealedCards = []
    return currentPlayer, bet, pot, round, firstBet, foldPlayersNumber, roundStart, revealedCards