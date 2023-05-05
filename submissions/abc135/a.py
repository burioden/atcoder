a, b = sorted(map(int, input().split()))

p = abs(a - b) // 2

if a + p == b - p:
  print(a + p)
else:
  print('IMPOSSIBLE')
