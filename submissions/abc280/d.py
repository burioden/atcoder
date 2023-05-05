import math

k = int(input())
i = 0

while i < 2e6:
  i += 1
  k //= math.gcd(k,i)
  if k < 2:
    print(i)
    exit()

print(k)
