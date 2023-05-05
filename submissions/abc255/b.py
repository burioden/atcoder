n,k = map(int,input().split())
a = list(map(int,input().split()))
s = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n):
  m = 1e18
  for l in a:
    m = min(m,(s[i][0] - s[l-1][0])**2 + (s[i][1] - s[l-1][1])**2)
  ans = max(ans,m)

print(ans**0.5)
