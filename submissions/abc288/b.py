n,k = map(int,input().split())
a = [input() for _ in range(n)]
b = sorted([a[i] for i in range(k)])

for i in b:
  print(i)
