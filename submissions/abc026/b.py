import math

n = int(input())
r = sorted([int(input()) for _ in range(n)],reverse=True)

ans = 0
i = 0
while i < n:
  if i%2 == 0:
    ans += r[i]**2
  else:
    ans -= r[i]**2
  i += 1

print("{:.6f}".format(ans*math.pi))
