n,x = map(int,input().split())
a = list(map(int,input().split()))

s = 0
for i in range(n):
  if i%2 == 0:
    s += a[i]
  else:
    s += a[i]-1
    
print('Yes' if s <= x else 'No')
