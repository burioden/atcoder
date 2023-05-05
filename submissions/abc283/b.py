n = int(input())
a = list(map(int,input().split()))
q = int(input())
for i in range(q):
  x,*y = map(int, input().split())
  if x == 1:
    a[y[0]-1] = y[1]
  else:
    print(a[y[0]-1])
