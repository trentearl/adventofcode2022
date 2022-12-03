
lines = [ l.strip() for l in open('./03.data', 'r').readlines() ]

print(lines)

def val(l):
    if l.islower():
        return 1 + ord(l) - ord('a')
    else:
        return 27 + ord(l) - ord('A')

ans = 0
for line in lines:
    N = len(line)
    shared = (set(line[:N // 2]) & set(line[N // 2:])).pop()
    print(shared, val(shared))
    ans += val(shared)

print(ans)
