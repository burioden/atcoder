n,x = map(int,input().split())

if abs(1-x) < abs(n-x):
  print(x-1)
else:
  print(n-x)
