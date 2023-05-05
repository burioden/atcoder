from itertools import product

n,m = map(int,input().split())
a = []

for i in range(m):
  c = int(input())
  d = list(map(int,input().split()))
  a.append(d)

cnt = 0

for bit in product((0,1),repeat=m):
  inner = []
  for i in range(m):
    if bit[i] == 1:
      inner.extend(a[i])
  if len(set(inner)) == n:
    cnt += 1
        
print(cnt)
