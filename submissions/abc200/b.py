n,k = map(int,input().split())

for i in range(k):
  if n%200 == 0:
    n //= 200
  else:
    x = str(n)
    y = x+'200'
    n = int(y)

print(n)
