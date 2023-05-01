n,k = map(int, input().split())

for i in range(k):
  if n%200 == 0:
    n = n//200
  else:
    n = int(str(n)+str(200))

print(n)
