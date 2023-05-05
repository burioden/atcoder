n = int(input())
c = []
m = []
for i in range(n):
  C,M = input().split()
  c.append(C)
  m.append(int(M))

if sum(m)/2 < max(m):
  print(c[m.index(max(m))])
else:
  print("atcoder")
