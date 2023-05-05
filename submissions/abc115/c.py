n,k = map(int,input().split())
h = sorted([int(input()) for _ in range(n)])

ans = 10**9
l,r = 0,k-1

while r < n:
  ans = min(ans,h[r]-h[l])
  r += 1
  l += 1
  
print(ans)
