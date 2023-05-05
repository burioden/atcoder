n,w = map(int,input().split())
a = sorted([list(map(int, input().split())) for _ in range(n)],reverse=True)

i = 0
ans = 0
while w >= 0 and i < n:
  if w <= a[i][1]:
    ans += (w*a[i][0])
    w -= a[i][1]
  else:
    ans += (a[i][0]*a[i][1])
    w -= a[i][1]
  i += 1

print(ans)
