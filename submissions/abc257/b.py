n,k,q = map(int,input().split())
a = list(map(int,input().split()))
L = list(map(int,input().split()))

l = list(map(lambda x: x-1,L))

for i in l:
  if a[i] <= n-1:
    if a[i]+1 not in a:
      a[i] += 1

print(*a)
