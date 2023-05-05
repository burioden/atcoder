n,m = map(int,input().split())
g = [[0]*n for _ in range(n)]
for _ in range(m):
    a,b = map(int,input().split())
    g[a-1][b-1] = 1
    g[b-1][a-1] = 1

cnt = 0
for i in range(n):
  for j in range(i+1,n):
    for l in range(j+1,n):
      if g[i][j] and g[j][l] and g[l][i]:
        cnt += 1
        
        
print(cnt)
