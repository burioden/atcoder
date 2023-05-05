n, t = map(int, input().split())
c = list(map(int, input().split()))
r = list(map(int, input().split()))
ma = []

if t in c:
  for i, d in enumerate(c):
    if d == t:
      ma.append([r[i], i + 1])

if t not in c:
  for i, d in enumerate(c):
    if d == c[0]:
      ma.append([r[i], i + 1])
      
ma.sort()

print(ma[-1][1])
