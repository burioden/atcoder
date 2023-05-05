n,a,b = map(int, input().split())

g = []
c = []
for i in range(n):
  inner = []
  if i % 2 == 0:
    for j in range(b):
      inner.append('.')
  elif i % 2 == 1:
    for j in range(b):
      inner.append('#')
  g.append(inner)
  
for i in range(n):
  inner = []
  if i % 2 == 0:
    for j in range(b):
      inner.append('#')
  elif i % 2 == 1:
    for j in range(b):
      inner.append('.')
  c.append(inner)
  
G = sum(g, [])
C = sum(c, [])

for i in range(n):
  if i % 2 == 0:
    for j in range(a):
      print(*G,sep='')
  else:
    for j in range(a):
      print(*C,sep='')
