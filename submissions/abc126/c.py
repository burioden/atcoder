from collections import defaultdict

n,k = map(int,input().split())

d = []

for i in range(1,n+1):
  cnt = 0
  j = i
  while j <= k-1:
    j *= 2
    cnt += 1
  d.append((1/n)*(1/(2**cnt)))

print(sum(d))
