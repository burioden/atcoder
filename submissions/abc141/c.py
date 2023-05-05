n,k,q = map(int,input().split())
a = [0 for _ in range(n)]

for i in range(q):
  m = int(input())
  a[m-1] += 1
  
for e in a:
  if k-q+e > 0:
    print('Yes')
  else:
    print('No')
