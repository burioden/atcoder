n,m = map(int,input().split())
a = [[] for _  in range(n)]
for i in range(m):
  x,*y = map(int,input().split())
  for j in range(x):
    for k in range(x):
      a[y[j]-1].append(y[k])
      
for i in a:
  if len(set(i)) < n:
    print('No')
    exit()

print('Yes')
