n = int(input())

ans = 0

for i in range(n+1):
  if pow(2,i) <= n:
    ans = pow(2,i)

print(ans)
