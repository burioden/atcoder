import collections

n = int(input())
a = list(map(int,input().split()))

b = collections.Counter(a)

c = 0

for i in b.items():
  c += (i[1] * (i[1]-1)) // 2
  
for i in range(n):
  print(c - ((b[a[i]] * (b[a[i]]-1)) // 2) + (((b[a[i]]-1) * (b[a[i]]-2)) // 2))
