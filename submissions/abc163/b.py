n,m = map(int,input().split())
a = list(map(int,input().split()))

for i in a:
  n -= i

print(n if n >= 0 else -1)
