
ITEM_SCORE = { 'rock': 1, 'paper': 2, 'scissors': 3 }
ROUND_SCORE = { 'loss': 0, 'draw': 3, 'win': 6 }
ITEM = { 'A': 'rock', 'B': 'paper', 'C': 'scissors' }
OUTCOME = { 'X': 'loss', 'Y': 'draw', 'Z': 'win' }
WINNERS = { 'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock' }
LOSERS = { 'rock': 'paper', 'scissors': 'rock', 'paper': 'scissors' }

lines = [ l.strip() for l in open('./02.data', 'r').readlines() ]
rounds = []

for line in lines:
    a, b = line.split(' ')
    rounds.append((ITEM[a], OUTCOME[b]))

scores = []
for r in rounds:
    them, outcome = r[0], r[1]
    score = ROUND_SCORE[outcome]

    if outcome == 'loss':
        item = WINNERS[them]
    elif outcome == 'draw':
        item = them
    else:
        item = LOSERS[them]

    scores.append(score + ITEM_SCORE[item])


print(sum(scores))

