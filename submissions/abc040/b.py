n = int(input())

ans = 1e18
for w in range(1,int(n**0.5+1)):
  h = n//w
  ans = min(ans,abs(h-w) + n%w)

print(ans)
