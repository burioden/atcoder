v, t, s, d = map(int, input().split())

x = d / v

if t <= x <= s:
  print('No')
else:
  print('Yes')
