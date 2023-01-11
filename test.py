from roundUtils import calculatePower

calculatePower([['A','♠'],['K','♠'],['Q','♠'],[10,'♠'],['J','♠'],[4,'♦'],[4,'♦']]) # ROYAL FLUSH
calculatePower([[10,'♠'],[8,'♠'],[7,'♠'],[9,'♠'],[4,'♦'],[6,'♠'],[4,'♦']]) # STRAIGHT FLUSH
calculatePower([[10,'♠'],[2,'♠'],[10,'♣'],[9,'♠'],[10,'♦'],[10,'♥'],[2,'♦']]) # 4 OF A KIND
calculatePower([[10,'♠'],[2,'♠'],[10,'♣'],[9,'♠'],[10,'♦'],[8,'♥'],[2,'♦']]) # FULL HOUSE
calculatePower([[10,'♠'],[2,'♠'],[5,'♠'],[5,'♠'],[4,'♦'],[5,'♠'],[3,'♦']]) # FLUSH
calculatePower([[10,'♠'],[8,'♥'],[7,'♠'],[9,'♠'],[4,'♦'],[6,'♠'],[4,'♦']]) # STRAIGHT
calculatePower([[10,'♠'],[2,'♠'],[10,'♣'],[9,'♠'],[10,'♦'],[8,'♥'],['A','♦']]) # 3 OF A KIND
calculatePower([[10,'♠'],[2,'♠'],[10,'♣'],[9,'♠'],[9,'♦'],[8,'♥'],['A','♦']]) # 2 PAIR
calculatePower([[10,'♠'],[2,'♠'],[7,'♣'],[9,'♠'],[9,'♦'],[8,'♥'],['A','♦']]) # PAIR
calculatePower([[10,'♠'],[2,'♠'],[7,'♣'],[9,'♠'],[4,'♦'],[8,'♥'],['A','♦']]) # HIGH
