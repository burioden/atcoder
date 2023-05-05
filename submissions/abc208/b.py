import math

p = int(input())

cnt = 0

for i in range(10,0,-1):
    while math.factorial(i) <= p:
      cnt += 1
      p -= math.factorial(i)

print(cnt)
