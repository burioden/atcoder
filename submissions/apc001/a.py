a, b = map(int, input().split())

if a % b == 0 or b == 1:
  print(-1)
else:
  print(a * (b - 1))
