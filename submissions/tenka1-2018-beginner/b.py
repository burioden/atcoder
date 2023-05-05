a,b,k = map(int, input().split())

for i in range(k):
  if i%2 == 1:
    a += b//2
    b //= 2
  else:
    b += a//2
    a //= 2

print(a,b)
