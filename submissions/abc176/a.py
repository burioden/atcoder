n, x, t = map(int, input().split())

a = n // x

if n % x > 0:
  a += 1

print(t * a)
