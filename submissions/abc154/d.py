n,k = map(int,input().split())
p = list(map(int,input().split()))

a = [0 for _ in range(n+1)]

for i in range(n):
  p[i] = ((p[i] + 1)/2)

for i in range(n):
  a[i+1] = a[i] + p[i]
  
b = [0 for i in range(n-k+1)]

for i in range(n-k+1):
  b[i] = a[i+k] - a[i]


print(max(b))
