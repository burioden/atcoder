from collections import defaultdict

n,q = map(int,input().split())
w = defaultdict(lambda :defaultdict(list))
for i in range(q):
  t,a,b = map(int,input().split())
  a -= 1
  b -= 1
  if t == 1:
    w[a][b] = 1
  elif t == 2:
    w[a][b] = 0
  elif t == 3:
    if w[a][b] and w[b][a]:
      print('Yes')
    else:
      print('No')
