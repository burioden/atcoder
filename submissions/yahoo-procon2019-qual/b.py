c = [0,0,0,0]
for i in range(3):
  x,y = map(int, input().split())
  x -= 1
  y -= 1
  c[x] += 1
  c[y] += 1
  
if c.count(2) == 2:
  print('YES')
else:
  print('NO')
