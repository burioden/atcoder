n,k = map(int,input().split())
a = sorted(list(map(int,input().split())),reverse=True)

for i in range(k if n > k else n):
  a[i] = 0

print(sum(a))
