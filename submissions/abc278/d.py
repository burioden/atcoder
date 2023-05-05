from collections import defaultdict

n = int(input())
a = list(map(int,input().split()))
q = int(input())
for i in range(q):
  x,*y = map(int,input().split())
  if x == 1:
    ad = y[0]
    a = defaultdict(lambda:ad)
  elif x == 2:
    a[y[0]-1] += y[1]
  elif x == 3:
    print(a[y[0]-1])
