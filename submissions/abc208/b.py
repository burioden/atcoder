p = int(input())

ans = 0

def fac(n):
  v = 1
  for i in range(n,1,-1):
    v *= i
  return v

for i in range(10,0,-1):
  while p >= fac(i):
    p -= fac(i)
    ans += 1

print(ans)
