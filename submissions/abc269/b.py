li = [input() for i in range(10)]

a = 100
b = 0
c = 100
d = 0

for i in range(10):
  for j in range(10):
    if li[i][j] == "#":
      a = min(a,i+1)
      b = max(b,i+1)
      c = min(c,j+1)
      d = max(d,j+1)

print(a,b)
print(c,d)
