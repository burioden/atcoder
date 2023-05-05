r,g,b,n = map(int, input().split())

cnt = 0
for i in range(n//r+1):
  for j in range(n//g+1):
    if (n-r*i-g*j)%b == 0 and n-r*i-g*j >= 0:
      cnt += 1
        
print(cnt)
