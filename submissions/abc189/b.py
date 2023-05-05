n, x = map(int, input().split())

alco = 0
x *= 100

for i in range(n):
  v, p = map(int, input().split())
  alco += (v * p)
  if x < alco:
    exit(print(i + 1))
    
print(-1)
