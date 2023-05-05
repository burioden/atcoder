n, m, a, b = map(int, input().split())
c = [int(input()) for _ in range(m)]


for day in range(m):
  if n <= a:
    n += b
  n -= c[day]
  if n < 0:
    exit(print(day + 1))

if day + 1 == m:
  if n >= 0:
    print('complete')
  else:
    print(m)
else:
  print(day + 1)
