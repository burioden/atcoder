s,t,x = map(int,input().split())

if s <= x < t:
  print('Yes')
elif x < t <= s:
  print('Yes')
elif t <= s <= x:
  print('Yes')
else:
  print('No')
