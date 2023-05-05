n = int(input())
a = []
b = []
for i in range(n):
  x, y = map(int, input().split())
  a.append(x)
  b.append(y)
  
d = max(a)
e = b[a.index(max(a))]

print(d + e)
