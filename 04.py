
def makeSections(s):
    a, b = s.split('-')
    return set(range(int(a), int(b) + 1))


jobs = [ list(map(makeSections, l.strip().split(','))) for l in open('./04.data', 'r').readlines() ]

ans = 0

for a, b in jobs:
    if a & b:
        ans += 1
print(ans)



