
ITEM_SCORE = { 'rock': 1, 'paper': 2, 'scissors': 3 }
ROUND_SCORE = { 'loss': 0, 'draw': 3, 'win': 6 }
ITEM = { 'A': 'rock', 'B': 'paper', 'C': 'scissors', 'X': 'rock', 'Y': 'paper', 'Z': 'scissors' }
WINNERS = { 'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock' }

lines = [ l.strip() for l in open('./02.data', 'r').readlines() ]
rounds = []

for line in lines:
    rounds.append(list(map(lambda k: ITEM[k], line.split(' '))))

score = []
for r in rounds:
    them, me = r[0], r[1]
    if WINNERS[them] == me:
        status = 'loss'
    elif them == me:
        status = 'draw'
    else:
        status = 'win'
    score.append(ROUND_SCORE[status] + ITEM_SCORE[me])


print(sum(score))

