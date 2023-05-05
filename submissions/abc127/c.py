n,m = map(int,input().split())
a = []
b = []
for i in range(m):
  A,B = map(int,input().split())
  a.append(A)
  b.append(B)

x = max(a)
y = min(b)

print(y-x+1 if y-x >=0 else 0)
