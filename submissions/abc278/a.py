n,k = map(int,input().split())
a = list(map(int,input().split()))

if n <= k:
   print(*[0]*n)
else:
  print(*a[k:]+[0]*k)
