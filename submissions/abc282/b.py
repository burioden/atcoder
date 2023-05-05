import math
n,m = map(int,input().split())
a = sorted([input() for _ in range(n)])

cnt = 0
for i in range(n):
  for j in range(i+1,n):
    for l in range(m):
      if a[i][l] == "x" and a[j][l] == "x":
        cnt += 1
        break
        
print(math.comb(n,2)-cnt)
