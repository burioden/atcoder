n = int(input())
m = int(n ** 0.5) + 2
cnt = set()
for a in range(2,m):
  for b in range(2,m):
    if a ** b > n:
      break
    cnt.add(a**b)

print(n - len(cnt))
