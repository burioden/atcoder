n, w = map(int, input().split())
a = list(map(int, input().split()))

good = set()

for i in range(n):
  if a[i] <= w:
        good.add(a[i])

for i in range(n):
  for j in range(i + 1, n):
    if a[i] + a[j] <= w:
      good.add(a[i] + a[j])
      
for i in range(n):
  for j in range(i + 1, n):
    for k in range(j + 1, n):
      if a[i] + a[j] + a[k] <= w:
        good.add(a[i] + a[j] + a[k])
        
print(len(good))
