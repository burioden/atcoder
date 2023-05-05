n, a, b = map(int, input().split())

ans = ''

while n > 0:
  n -= a
  ans = 'Ant'
  if n > 0:
    n -= b
    ans = 'Bug'
    
print(ans)
    
