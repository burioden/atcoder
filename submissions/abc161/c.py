n,k = map(int,input().split())

if n < k:
  print(min(k-n,n))
  exit()
elif n%k == 0 or n == 0:
  print(0)
  exit()

print(abs((n%k)-k))
