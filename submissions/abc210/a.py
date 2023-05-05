n, a, x, y = map(int, input().split())

ans = 0

while n > 0 and a > 0:
  ans += x
  n -= 1
  a -= 1

if n > 0:
  ans += (n * y)
  
print(ans)
