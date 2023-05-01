n,m = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(m)]

ans = [0]*n

for i in range(m):
  for k in range(2):
    for l in range(1,n+1):
      if li[i][k] == l:
        ans[l-1] += 1

print(*ans,sep='\n')
