A = [input() for _ in range(10)]
# B = zip(*a)

a,b,c,d = 11,-1,11,-1
for i in range(10):
  for j in range(10):
    if A[i][j] == "#":
      a = min(i,a)
      b = max(i,b)
      c = min(j,c)
      d = max(j,d)

print(a+1,b+1)
print(c+1,d+1)
