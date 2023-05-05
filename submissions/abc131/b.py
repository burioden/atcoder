n,l = map(int,input().split())

ringo = []

for i in range(1,n+1):
  ringo.append(i+l-1)

r = sum(ringo)
x = 10**9

for i in ringo:
  x = min(x,abs(i))

if r < 0:
  print(r+x)
else:
  print(r-x)
