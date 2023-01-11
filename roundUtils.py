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
    global combination

    global flushFlag
    flushFlag = False

    findSameCards(allCards)
    findSameSigns(allCards)
    findConsecutiveCards(allCards)
    print(combination)

def findSameCards(allCards):
    sameCards = OrderedDict()
    for i in range(7):
        if str(allCards[i][0]) in sameCards:
            sameCards[str(allCards[i][0])] += 1
        else:
            sameCards[str(allCards[i][0])] = 1
    
    global combination
    global power
    global leadingValue
    pairCount = 0
    fullHousePossibilityStrong = False
    fullHousePossibilityWeak = False
    for value in sameCards.keys():
        if sameCards[value] == 4 and power < POWERS['FOUR OF A KIND']:
            power = POWERS['FOUR OF A KIND']
            leadingValue = int(value)
            combination = "FOUR OF A KIND WITH " + giveName(leadingValue)
        elif sameCards[value] == 3 and power < POWERS['THREE OF A KIND']:
            power = POWERS['THREE OF A KIND']
            leadingValue = int(value)
            combination = "THREE OF A KIND WITH " + giveName(leadingValue)
            
            fullHousePossibilityStrong = True
        elif sameCards[value] == 2: 
            if power < POWERS['PAIR']:
                power = POWERS['PAIR']
                leadingValue = int(value)
                combination = "PAIR WITH " + giveName(leadingValue)

            pairCount += 1
            if pairCount > 1:
                power = POWERS['TWO PAIR']
                combination = "TWO PAIR WITH " + giveName(leadingValue)

            fullHousePossibilityWeak = True
        elif power <= POWERS['HIGH'] and sameCards[value] == 1 and leadingValue < int(value):
            power = POWERS['HIGH']
            leadingValue = int(value)
            combination = "HIGH CARD WITH " + giveName(leadingValue)

    if fullHousePossibilityStrong and fullHousePossibilityWeak and power <= POWERS['FULL HOUSE']:
        power = POWERS['FULL HOUSE']
        combination = "FULL HOUSE WITH " + giveName(leadingValue)

def findSameSigns(allCards):
    sameSigns = {}
    for i in range(7):
        if allCards[i][1] in sameSigns:
            sameSigns[allCards[i][1]] += 1
        else:
            sameSigns[allCards[i][1]] = 1

    global combination
    global power
    global leadingValue
    global flushFlag
    flushFlag = ""

    for sign in sameSigns.keys():
        if sameSigns[sign] > 4 and power < POWERS['FLUSH']:
            power = POWERS['FLUSH']
            combination = "FLUSH WITH " + sign
            flushFlag = sign

def findConsecutiveCards(allCards):
    global combination
    global power
    global leadingValue
    global flushFlag

    distinct = []
    for i in range(7):
        if not allCards[i] in distinct:
            distinct.append(allCards[i][0])

    end = distinct[0]
    tempLeadingValue = distinct[0]
    count = 1
    position = 0
    consecutiveFlag = False
    while position < len(distinct) - 1 and count < 5:
        position += 1
        if distinct[position] == end - 1:
            count += 1
        else:
            count = 1
            tempLeadingValue = distinct[position]
        end = distinct[position]
    
    if count == 5:
        consecutiveFlag = True

    if power < POWERS['ROYAL FLUSH'] and consecutiveFlag and flushFlag and int(tempLeadingValue) == 14:
        power = POWERS['ROYAL FLUSH']
        leadingValue = tempLeadingValue
        combination = "ROYAL FLUSH ON " + flushFlag
    elif power < POWERS['STRAIGHT FLUSH'] and consecutiveFlag and flushFlag:
        power = POWERS['STRAIGHT FLUSH']
        leadingValue = tempLeadingValue
        combination = "STRAIGHT FLUSH ON " + giveName(leadingValue) + flushFlag
    elif power < POWERS['STRAIGHT'] and consecutiveFlag:
        power = POWERS['STRAIGHT']
        leadingValue = tempLeadingValue
        combination = "STRAIGHT ON " + giveName(leadingValue)