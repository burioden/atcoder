n,k = map(int,input().split())

cnt = 0

for i in range(1,n+1):
  for j in range(1,n+1):
    z = k-i-j
    if z > 0 and z <= n:
      cnt += 1

print(cnt)
