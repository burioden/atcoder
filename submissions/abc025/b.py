n,a,b = map(int,input().split())
s = 0
for i in range(n):
  x,y = input().split()
  y = int(y)
  if x == "East":
    if a <= y <= b:
      s += y
    elif y < a:
      s += a
    elif y > b:
      s += b
  else:
    if a <= y <= b:
      s -= y
    elif y < a:
      s -= a
    elif y > b:
      s -= b

if s == 0:
  print(0)
elif s < 0:
  print("West",abs(s))
else:
  print("East",s)
