n,x = map(int,input().split())
a = [0]+list(map(int,input().split()))

l = [0]*(n+1)

l[x] = 1
y = a[x]
for i in range(n+1):
  l[y] = 1
  y = a[y]

print(l.count(1))
