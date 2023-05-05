a,b = map(int,input().split())

min = 1*a
max = 6*a

if min <= b <= max:
  print('Yes')
else:
  print('No')
