a,b = map(int,input().split())

if abs(a) > abs(b):
  print('Bug')
elif abs(a) < abs(b):
  print('Ant')
else:
  print('Draw')
