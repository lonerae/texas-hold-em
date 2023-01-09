from utils import *
from roundUtils import *

BIG_BLIND_BET = 10
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
        playerHands = serveCards(numberOfPlayers, deck)
        playerBets = instantiateBets(numberOfPlayers)

        currentPlayer, bet, pot, round, firstBet, foldPlayersNumber, roundStart, revealedCards = resetGame(bigBlindPlayer)

        while round < ROUND_NUMBER:
            if roundStart:
                print("=====ROUND",round+1,"=====")
                print("\n")
                revealedCards = reveal(deck, revealedCards, round)

                circle = 0
                roundStart = False

            if playerHands[currentPlayer]: # if player hasn't folded
                
                if revealedCards:
                    print("=====REVEALED=====")
                    print("\n")
                    printCards(revealedCards)
                    print("\n")
                    print("==================")
                    print("\n")

                printCards(playerHands[currentPlayer])

                if firstBet:
                    print("Player",bigBlindPlayer+1,"you start the bets with",BIG_BLIND_BET)
                    playerBet = BIG_BLIND_BET
                    firstBet = False
                    lead = bigBlindPlayer
                else:
                    print("Current bet is",bet)
                    print("Player",currentPlayer+1,"you have betted",playerBets[currentPlayer])
                    print("Place your bet or -1 to fold")
                    playerBet = int(input())

                    while playerBets[currentPlayer] + playerBet < bet and playerBet != -1:
                        print("Player",currentPlayer+1,"place your bet or -1 to fold")
                        playerBet = int(input())
                    
                if playerBet == -1:
                    fold(playerHands, playerBets, currentPlayer)
                    foldPlayersNumber += 1
                else:
                    checkOrRaise(playerBets, playerCapitals, pot, playerBet, currentPlayer)
                    
                if playerBets[currentPlayer] > bet:
                    bet = playerBets[currentPlayer]
                    lead = currentPlayer
                        
                print("Money remaining:",playerCapitals[currentPlayer],"\n")
                circle += 1

            if endRound(numberOfPlayers, foldPlayersNumber, bet, playerBets, circle, lead, currentPlayer):
                round += 1
                roundStart = True
                lead = bigBlindPlayer
                currentPlayer = bigBlindPlayer
            else:
                currentPlayer = (currentPlayer + 1) % numberOfPlayers

            if foldPlayersNumber == numberOfPlayers -1:
                break;    

        for currentPlayer in range(numberOfPlayers):
            if playerHands[currentPlayer]:
                calculatePower(playerHands[currentPlayer] + revealedCards)
                
        
        game += 1
        bigBlindPlayer = (bigBlindPlayer + 1) % numberOfPlayers

main()