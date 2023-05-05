n,m = map(int,input().split())
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(m)]

c = []

for i,d in a:
  inner = []
  for x,y in b:
    inner.append(abs(i-x) + abs(d-y))
  c.append(inner)

for i in c:
  print(i.index(min(i))+1)
