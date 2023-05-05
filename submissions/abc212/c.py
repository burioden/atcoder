n,m = map(int,input().split())
a = sorted(list(map(int,input().split())))
b = sorted(list(map(int,input().split())))

i,j = 0,0

ans = 10**9

while i<n and j<m:
  ans = min(ans,abs(a[i]-b[j]))
  if a[i] < b[j]:
    i += 1
  else:
    j += 1
    
print(ans)
