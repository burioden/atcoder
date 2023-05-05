a,b,c,x = map(int, input().split())

if x > b:
  print(0)
elif b >= x > a:
  print(c/(b-a))
elif x <= a:
  print(1)
