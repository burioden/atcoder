n = int(input())
a = [i for i in range(2,2*n+2)]
print(1)

for i in range(n):
  x = int(input())
  a.remove(x)
  y = a.pop()
  print(y)
