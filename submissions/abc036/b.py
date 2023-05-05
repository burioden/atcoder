n = int(input())
a = [list(input()) for _ in range(n)]

b = []

for i in range(n):
  inner = []
  for j in reversed(range(n)):
    inner.append(a[j][i])
  b.append(inner)

for i in b:
  print(*i,sep="")
