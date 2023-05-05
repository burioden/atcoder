n,m = map(int,input().split())
a = []
for i in range(n):
  x,y = map(int, input().split())
  if y <= m:
    a.append(x)

s = len(a)

print(min(a) if s > 0 else "TLE")
