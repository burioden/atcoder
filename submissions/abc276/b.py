n,m = map(int,input().split())
li = [[] for _ in range(n)]

for i in range(m):
  A,B = map(int,input().split())
  li[A-1].append(B)
  li[B-1].append(A)

for i in li:
  i = sorted(i)
  print(len(i), *i)
