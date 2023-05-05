n, r = map(int, input().split())

if n >= 10:
  print(r)
else:
  p = (100 * (10 - n))
  print(r + p)
