import math

k = int(input())

cnt = 0
for i in range(1,k+1):
  for j in range(1,k+1):
    g = math.gcd(i,j)
    for l in range(1,k+1):
      cnt += math.gcd(g,l)

print(cnt)
