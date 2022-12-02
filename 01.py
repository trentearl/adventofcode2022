
lines = [ l.strip() for l in open('./01.data', 'r').readlines() ]

cur = ans = 0
while lines:
    line = lines.pop()
    if line:
        cur += int(line)
        ans = max(ans, cur)
    else:
        cur = 0

print(ans)
