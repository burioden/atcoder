n, m = map(int, input().split())

if n * n < m:
  exit(print(-1))

x = int(m ** 0.5)
d = []

for a in range(1, x + 2):
  b = (a + m - 1) // a
  if 1 <= a <= n:
    if 1 <= b <= n:
      if m <= a * b:
        d.append(a * b)

print(min(d) if len(d) > 0 else -1)
