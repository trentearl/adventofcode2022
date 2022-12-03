
lines = [ l.strip() for l in open('./03.data', 'r').readlines() ]

def val(l):
    if l.islower():
        return 1 + ord(l) - ord('a')
    else:
        return 27 + ord(l) - ord('A')

ans = 0
buf = []
for line in lines:
    buf.append(set(line))

    if len(buf) == 3:
        v = val((buf[0] & buf[1] & buf[2]).pop())
        ans += v
        buf = []

print(ans)

