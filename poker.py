import random

FIGURES = ['J','Q','K']
VALUES = list(range(1,11)) + FIGURES
SIGNS = ['♡','♤','♧','♢']

BIG_BLIND_BET = 10
CAPITAL = 1000
INITIAL_BIG_BLIND_PLAYER = 0
ROUND_NUMBER = 5

def main():
    numberOfPlayers = int(input("How many will be playing? "))
    playerCapitals = instantiateCapitals(numberOfPlayers)
    
    global bigBlindPlayer, currentPlayer, bet, pot, round, firstBet, foldPlayersNumber, roundStart, revealedCards
    bigBlindPlayer = INITIAL_BIG_BLIND_PLAYER

    game = 1
    while capitalRemains(playerCapitals,numberOfPlayers):
        print("=====GAME",game,"BEGINS=====")
        print("\n")

        deck = shuffleDeck()
        playerBets = instantiateBets(numberOfPlayers)
        playerHands = serveCards(numberOfPlayers, deck)

        resetGame()

        while round < ROUND_NUMBER:
            if roundStart:
                print("=====ROUND",round+1,"=====")
                print("\n")

                revealedCards = reveal(deck, revealedCards, round)
                if revealedCards:
                    print(revealedCards)
                    print("\n")
                
                circle = 0
                roundStart = False

            if playerHands[currentPlayer]: # if player hasn't folded
                print(playerHands[currentPlayer])

                if currentPlayer == bigBlindPlayer and firstBet:

                    print("Player",bigBlindPlayer+1,"you start the bets with",BIG_BLIND_BET,"\n")
                    playerBets[currentPlayer] += BIG_BLIND_BET
                    firstBet = False
                    lead = bigBlindPlayer

                else:

                    print("Current bet is",bet)
                    print("Player",currentPlayer+1,"you have betted",playerBets[currentPlayer])
                    print("Place your bet or -1 to fold")
                    playerBet = int(input())
                    # INVALID BETS
                    while playerBets[currentPlayer] + playerBet < bet and playerBet != -1:
                        print("Player",currentPlayer+1,"place your bet or -1 to fold")
                        playerBet = int(input())
                    
                    print("\n")

                    if playerBet == -1:
                        fold(playerHands, playerCapitals, playerBets, currentPlayer)
                        foldPlayersNumber += 1
                    else:
                        playerBets[currentPlayer] += playerBet
                        pot += playerBet

                    if playerBets[currentPlayer] > bet:
                        bet = playerBets[currentPlayer]
                        lead = currentPlayer # PLAYER WITH HIGHEST BET

                circle += 1

            # IF ALL PLAYERS WHO HAVEN'T FOLDED HAVE BETTED THE SAME AND A FULL CIRCLE IS COMPLETED
            if (
                    playerBets.count(bet) == numberOfPlayers - foldPlayersNumber and
                    lead == (currentPlayer + 1) % numberOfPlayers and
                    circle >= numberOfPlayers - foldPlayersNumber
                ):

                round += 1
                roundStart = True
                lead = bigBlindPlayer
                currentPlayer = bigBlindPlayer - 1 # bigBlindPlayer after increment

            currentPlayer += 1
            if currentPlayer == numberOfPlayers:
                currentPlayer = 0

            # IF ALL BUT ONE FOLD, A NEW GAME STARTS
            if foldPlayersNumber == numberOfPlayers -1:
                break;    

        # UPDATE THE CAPITALS OF ALL PLAYERS WHO STAYED UNTIL THE END
        for currentPlayer in range(numberOfPlayers):
            if playerHands[currentPlayer]:
                calculatePower(playerHands[currentPlayer] + revealedCards)
                playerCapitals[currentPlayer] -= playerBets[currentPlayer]
        
        print(pot)
        game += 1
        bigBlindPlayer += 1

def instantiateCapitals(numberOfPlayers):
    playerCapitals = []
    for i in range(0,numberOfPlayers):
            playerCapitals.append(CAPITAL)
    return playerCapitals

def instantiateBets(numberOfPlayers):
    playerBets = []
    for p in range(0,numberOfPlayers):
        playerBets.append(0)
    return playerBets

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

def resetGame():
    global bigBlindPlayer
    global currentPlayer
    currentPlayer = bigBlindPlayer
    global bet
    bet = BIG_BLIND_BET
    global pot
    pot = BIG_BLIND_BET
    global round
    round = 0
    global firstBet
    firstBet = True
    global foldPlayersNumber
    foldPlayersNumber = 0
    global roundStart
    roundStart = True
    global revealedCards
    revealedCards = []

def reveal(deck, revealed, round):
    if (round == 1):
        deck.pop()
        for i in range(3):
            revealed.append(deck.pop())
    elif round == 2 or round == 3:
        deck.pop()
        revealed.append(deck.pop())
    return revealed

def fold(playerHands, playerCapitals, playerBets, currentPlayer):
    playerHands[currentPlayer] = []
    playerCapitals[currentPlayer] -= playerBets[currentPlayer]
    playerBets[currentPlayer] = 0

    return playerHands, playerCapitals, playerBets

def calculatePower(allCards):
    print(allCards)

main()