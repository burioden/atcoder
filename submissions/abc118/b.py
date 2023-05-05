n,m = map(int,input().split())
k = set([i for i in range(1,m+1)])
for i in range(n):
  x,*y = map(int,input().split())
  k&=set(y)

print(len(k))
