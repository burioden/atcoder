h,w = map(int,input().split())

nya = 101
a = []
for i in range(h):
  x = list(map(int,input().split()))
  y = min(x)
  nya = min(y,nya)
  a.append(x)

ans = 0
for i in range(h):
  for j in range(w):
    if a[i][j] > nya:
      ans += (a[i][j] - nya)
      
print(ans)
