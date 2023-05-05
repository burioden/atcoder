n,q = map(int,input().split())
a = [0]*n
for i in range(q):
  x,y,z = map(int, input().split())
  for j in range(x-1,y):
    a[j] = z

print(*a,sep="\n")
