s = list(input())
a, b, c, d = map(int, input().split())

b += 1
c += 2
d += 3

s[a:a], s[b:b], s[c:c], s[d:d] = '"', '"', '"', '"'

print(*s, sep='')
