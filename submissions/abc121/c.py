n,m = map(int,input().split())
li = sorted([list(map(int, input().split())) for _ in range(n)])

ans = 0
while m >= 0:
  for x,y in li:
    if m >= y:
      ans += x*y
      m -= y
    elif y > m >= 0:
      ans += m*x
      m -= y
    else:
      break

print(ans)
