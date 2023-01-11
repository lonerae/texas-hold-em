from collections import OrderedDict

POWERS = {'HIGH':1,'PAIR':2,'TWO PAIR':3,'THREE OF A KIND':4,'STRAIGHT':5,'FLUSH':6,'FULL HOUSE':7,'FOUR OF A KIND':8,'STRAIGHT FLUSH':9,'ROYAL FLUSH':10}

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

def giveValue(card):
    if card[0] == 'J':
        card[0] = 11
    elif card[0] == 'Q':
        card[0] = 12
    elif card[0] == 'K':
        card[0] = 13
    elif card[0] == 'A':
        card[0] = 14

def giveName(value):
    if value == 11:
        value = 'J'
    elif value == 12:
        value = 'Q'
    elif value == 13:
        value = 'K'
    elif value == 14:
        value = 'A'
    else:
        value = str(value)
    return value

def compare(x,y):
    return x[0]-y[0]

def calculatePower(allCards):
    for card in allCards:
        giveValue(card)

    allCards = sorted(allCards, key=lambda card: card[0], reverse=True)
    print(allCards)

    global power
    power = 0
    global leadingValue
    leadingValue = 0
    combination = findSameCards(allCards)
    print(combination)
    # find(consecutiveCards)
    # find(sameSigns)

def findSameCards(allCards):
    sameCards = OrderedDict()
    for i in range(7):
        if str(allCards[i][0]) in sameCards:
            sameCards[str(allCards[i][0])] += 1
        else:
            sameCards[str(allCards[i][0])] = 1
    
    global power
    global leadingValue
    pairCount = 0
    fullHousePossibilityStrong = False
    fullHousePossibilityWeak = False
    for value in sameCards.keys():
        if sameCards[value] == 4 and power < POWERS['FOUR OF A KIND']:
            power = POWERS['FOUR OF A KIND']
            leadingValue = int(value)
            comb = "FOUR OF A KIND WITH " + giveName(value)
        elif sameCards[value] == 3 and power < POWERS['THREE OF A KIND']:
            power = POWERS['THREE OF A KIND']
            leadingValue = int(value)
            comb = "THREE OF A KIND WITH " + giveName(value)
            
            fullHousePossibilityStrong = True
        elif sameCards[value] == 2: 
            if power < POWERS['PAIR']:
                power = POWERS['PAIR']
                leadingValue = int(value)
                comb = "PAIR WITH " + giveName(value)

            pairCount += 1
            if pairCount > 1:
                power = POWERS['TWO PAIR']
                comb = "TWO PAIR WITH " + giveName(leadingValue)

            fullHousePossibilityWeak = True
        elif power <= POWERS['HIGH'] and sameCards[value] == 1 and leadingValue < int(value):
            power = POWERS['HIGH']
            leadingValue = int(value)
            comb = "HIGH CARD WITH " + giveName(value)

    if fullHousePossibilityStrong and fullHousePossibilityWeak and power <= POWERS['FULL HOUSE']:
        power = POWERS['FULL HOUSE']
        comb = "FULL HOUSE WITH " + giveName(leadingValue)

    return comb
