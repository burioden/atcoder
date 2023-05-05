h,w = map(int,input().split())
a = [list(map(int, input().split())) for _ in range(h)]

x = [sum(i) for i in a]
y = [sum(i) for i in zip(*a)]

ans = []
for i in range(h):
  inner = []
  for j in range(w):
    inner.append(x[i] + y[j] - a[i][j])
  ans.append(inner)
  
for i in ans:
  print(*i)
